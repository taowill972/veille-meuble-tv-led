# -*- coding: utf-8 -*-
"""
fetch_and_rank_led_tv.py
Pipeline d'extraction temps réel, analyse cognitive et scoring /100
spécifique aux meubles TV avec éclairage LED intégré (Leboncoin - Athis-Mons 25km).
"""

import os
import sys
import json
import math
import time
import base64
import re
import urllib.request
import urllib.parse
from datetime import datetime

ATHIS_LAT = 48.70773
ATHIS_LNG = 2.38881

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)
PARENT_SCRIPTS = os.path.join(os.path.dirname(BASE_DIR), "scripts")
if PARENT_SCRIPTS not in sys.path:
    sys.path.insert(0, PARENT_SCRIPTS)

DATA_DIR = os.path.join(BASE_DIR, "data")
PHOTOS_DIR = os.path.join(BASE_DIR, "photos")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(PHOTOS_DIR, exist_ok=True)

from lbc_scraper import fetch_search_ads, parse_ad_fields, haversine_distance

def download_image_b64(url: str, save_path: str = None) -> str:
    if not url:
        return ""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = resp.read()
            if save_path:
                with open(save_path, "wb") as f:
                    f.write(data)
            mime = "image/jpeg"
            if ".png" in url:
                mime = "image/png"
            elif ".webp" in url:
                mime = "image/webp"
            return f"data:{mime};base64," + base64.b64encode(data).decode("utf-8")
    except Exception as e:
        print(f"  [Image] Erreur b64 {url[:45]}: {e}")
        return ""

def extract_dimensions(text: str):
    length = None
    depth = None
    height = None
    
    m_dim3 = re.search(r'(\d{2,3})\s*(?:x|×|\*)\s*(\d{2,3})\s*(?:x|×|\*)\s*(\d{2,3})', text)
    if m_dim3:
        dims = [int(x) for x in m_dim3.groups()]
        length = max(dims)
        height = min(dims)
        depth = sorted(dims)[1]
        return length, depth, height

    m_l = re.search(r'(?:longueur|largeur|long|larg|l\s*:|l\s*=)\s*[:=]?\s*(\d{2,3})\s*(?:cm|m)?', text, re.IGNORECASE)
    if m_l:
        val = int(m_l.group(1))
        if val < 3:
            val = int(val * 100)
        if 80 <= val <= 260:
            length = val

    if not length:
        m_cm = re.search(r'(\d{2,3})\s*cm', text, re.IGNORECASE)
        if m_cm:
            val = int(m_cm.group(1))
            if 100 <= val <= 220:
                length = val

    return length, depth, height

def score_led_furniture(ad: dict) -> dict:
    title = ad.get("title", "")
    body = ad.get("body", "")
    full_text = (title + " " + body).lower()
    price = ad.get("price", 0)
    dist = ad.get("dist", 999.0)
    
    length, depth, height = extract_dimensions(full_text)
    
    # 1. Système LED & Télécommande (25 pts)
    led_score = 0
    led_details = []
    has_remote = any(w in full_text for w in ["telecommande", "télécommande", "remote", "rgb", "couleurs", "couleur", "variateur", "multi"])
    has_glass_clips = any(w in full_text for w in ["verre", "étagère en verre", "etagere en verre", "clips led", "tablette verre"])
    has_led_strip = any(w in full_text for w in ["ruban", "bandeau", "contour led", "eclairage led", "éclairage led", "lumineux", "lumière"])

    if has_remote:
        led_score += 25
        led_details.append("Ruban LED RGB Multicouleur avec télécommande")
        remote_status = "Télécommande RGB Incluse"
    elif has_glass_clips:
        led_score += 20
        led_details.append("Clips LED sur étagères en verre trempé")
        remote_status = "Clips LED Verre (Alimentation secteur)"
    elif has_led_strip or "led" in full_text:
        led_score += 18
        led_details.append("Éclairage LED intégré moderne")
        remote_status = "LED intégrée (Interrupteur / Prise)"
    else:
        led_score += 10
        led_details.append("Éclairage d'appoint")
        remote_status = "Standard"

    # 2. Rapport Qualité/Prix & Cote d'Occasion (25 pts)
    msrp = 240
    if length and length >= 160:
        msrp = 290
    elif length and length <= 120:
        msrp = 180
        
    discount = round((1.0 - (price / max(msrp, 1))) * 100)
    
    if price <= 45:
        price_score = 25
        bargain_level = "Très bonne affaire"
        bargain_gauge = "🟢 🟢 🟢 🟢"
    elif price <= 75:
        price_score = 22
        bargain_level = "Très bonne affaire"
        bargain_gauge = "🟢 🟢 🟢 🟢"
    elif price <= 100:
        price_score = 18
        bargain_level = "Bonne affaire"
        bargain_gauge = "🟢 🟢 🟢 ⚪"
    elif price <= 130:
        price_score = 14
        bargain_level = "Prix équitable"
        bargain_gauge = "🟡 🟡 ⚪ ⚪"
    else:
        price_score = 10
        bargain_level = "Prix élevé"
        bargain_gauge = "🔴 ⚪ ⚪ ⚪"

    # 3. Format & Logistique Scénic III / TV 55" (20 pts)
    logistics_score = 0
    dim_str = f"L {length or '130 (estimée)'} cm"
    if depth and height:
        dim_str += f" × P {depth} cm × H {height} cm"

    l_val = length or 135
    if l_val <= 140:
        logistics_score += 15
        scenic_compatible = "Conforme Scénic III (≤ 140 cm, direct)"
    elif l_val <= 160:
        logistics_score += 11
        scenic_compatible = "Scénic III (Sièges rabattus / Hayon)"
    else:
        logistics_score += 7
        scenic_compatible = "Démontage ou barres de toit conseillé"

    if dist <= 12.0:
        logistics_score += 5
    elif dist <= 18.0:
        logistics_score += 4
    elif dist <= 25.0:
        logistics_score += 2

    # 4. Rangements Multimédia & Passe-Câbles (15 pts)
    has_niches = any(w in full_text for w in ["niche", "étagère", "etagere", "console", "box", "ps5", "ouvert"])
    has_doors_drawers = any(w in full_text for w in ["tiroir", "porte", "portes", "placard", "fermé", "ferme", "rangement"])

    if has_niches and has_doors_drawers:
        storage_score = 15
        storage_desc = "Mixte parfait : Niches ouvertes (Box/PS5) + Portes fermées"
    elif has_doors_drawers:
        storage_score = 12
        storage_desc = "Caissons fermés (câbles dissimulés)"
    elif has_niches:
        storage_score = 11
        storage_desc = "Niches ouvertes multimédia"
    else:
        storage_score = 10
        storage_desc = "Rangement standard"

    # 5. État Esthétique & Finitions (15 pts)
    is_white_gloss = any(w in full_text for w in ["laqué", "laque", "brillant", "gloss", "blanc laqué", "blanc laque"])
    is_wood_white = any(w in full_text for w in ["chêne", "chene", "bois", "scandinave", "effet bois"])
    is_black_gloss = any(w in full_text for w in ["noir laqué", "noir laque", "noir brillant"])

    if is_white_gloss:
        finish_score = 15
        finish_name = "Blanc Laqué Brillant (High Gloss)"
    elif is_wood_white:
        finish_score = 14
        finish_name = "Bi-matière Bois Clair & Blanc Scandinave"
    elif is_black_gloss or "noir" in full_text:
        finish_score = 13
        finish_name = "Noir Laqué / Finition Moderne"
    else:
        finish_score = 11
        finish_name = "Finition Moderne Contemporaine"

    total_score = min(100, led_score + price_score + logistics_score + storage_score + finish_score)

    return {
        "score": total_score,
        "subscores": {
            "led": led_score,
            "price": price_score,
            "logistics": logistics_score,
            "storage": storage_score,
            "finish": finish_score
        },
        "msrp": msrp,
        "discount": discount,
        "bargain_level": bargain_level,
        "bargain_gauge": bargain_gauge,
        "led_type": " · ".join(led_details),
        "remote_status": remote_status,
        "scenic_status": scenic_compatible,
        "dimensions_str": dim_str,
        "length_cm": l_val,
        "finish_name": finish_name,
        "storage_desc": storage_desc
    }

def run_extraction_and_ranking():
    print("=== Démarrage Pipeline Meuble TV à LED (Athis-Mons 25km) ===")
    
    url1 = "https://www.leboncoin.fr/recherche?category=19&text=meuble+tv+led&locations=Athis-Mons_91200__48.70773_2.38881_2665_25000&price=15-150&owner_type=all&sort=time&order=desc"
    
    raw_ads_1 = fetch_search_ads(url1, max_pages=2)
    
    combined_raw = {}
    for a in raw_ads_1:
        aid = str(a.get("list_id"))
        if aid and aid not in combined_raw:
            combined_raw[aid] = a

    print(f"Total annonces brutes collectées sans doublon : {len(combined_raw)}")
    
    raw_file = os.path.join(DATA_DIR, "meuble_tv_led_raw_ads.json")
    with open(raw_file, "w", encoding="utf-8") as f:
        json.dump(list(combined_raw.values()), f, ensure_ascii=False, indent=2)

    parsed_ads = []
    excluded_ads = []

    for aid, raw in combined_raw.items():
        p = parse_ad_fields(raw)
        # Filtre de sincérité technique : éliminer les supports TV, bras articulés ou accessoires non-meubles
        title_lower = p.get("title", "").lower()
        if any(bad in title_lower for bad in ["support tv", "support mural", "support plafond", "pied tv seul", "bras articulé", "vesa"]):
            excluded_ads.append({
                "id": p["id"],
                "title": p["title"],
                "price": p["price"],
                "city": p["city"],
                "reason": "Accessoire / Support TV non meuble (support mural ou plafond VESA)"
            })
            continue

        txt = (p.get("title", "") + " " + p.get("body", "")).lower()
        
        if not any(k in txt for k in ["led", "lumiere", "lumière", "lumineux", "éclairage", "eclairage", "ruban"]):
            excluded_ads.append({
                "id": p["id"],
                "title": p["title"],
                "price": p["price"],
                "city": p["city"],
                "reason": "Absence avérée d'éclairage LED (fausse correspondance sémantique)"
            })
            continue

        if p["price"] < 15 or p["price"] > 160:
            excluded_ads.append({
                "id": p["id"],
                "title": p["title"],
                "price": p["price"],
                "city": p["city"],
                "reason": f"Prix hors budget cible ({p['price']} € vs cible 15-150€)"
            })
            continue

        analysis = score_led_furniture(p)
        p.update(analysis)
        parsed_ads.append(p)

    parsed_ads.sort(key=lambda x: (-x["score"], x["price"], x.get("dist") or 999))
    print(f"Total annonces qualifiées et notées : {len(parsed_ads)}")
    print(f"Total annonces exclues : {len(excluded_ads)}")

    print("\n--- Téléchargement & Encodage Base64 des photos des TOP candidats ---")
    top_candidates = parsed_ads[:10]
    
    for rank, item in enumerate(top_candidates, 1):
        item["rank"] = rank
        item["b64_images"] = []
        item_id = item["id"]
        ad_photos_dir = os.path.join(PHOTOS_DIR, item_id)
        os.makedirs(ad_photos_dir, exist_ok=True)
        
        print(f"  [#{rank} - Score {item['score']}/100] {item['title'][:40]} ({item['price']}€, {item['city']})")
        for idx, img_url in enumerate(item.get("images", [])[:3]):
            img_path = os.path.join(ad_photos_dir, f"photo_{idx+1}.jpg")
            b64_data = download_image_b64(img_url, img_path)
            if b64_data:
                item["b64_images"].append(b64_data)
        
        item["main_image_b64"] = item["b64_images"][0] if item["b64_images"] else ""

    scored_file = os.path.join(DATA_DIR, "meuble_tv_led_listings.json")
    with open(scored_file, "w", encoding="utf-8") as f:
        json.dump(top_candidates, f, ensure_ascii=False, indent=2)

    excl_file = os.path.join(DATA_DIR, "meuble_tv_led_excluded.json")
    with open(excl_file, "w", encoding="utf-8") as f:
        json.dump(excluded_ads, f, ensure_ascii=False, indent=2)

    prices = [p["price"] for p in parsed_ads if p["price"] > 0]
    avg_price = round(sum(prices) / len(prices), 1) if prices else 75.0
    sorted_prices = sorted(prices)
    median_price = sorted_prices[len(sorted_prices) // 2] if sorted_prices else 75.0
    min_price = min(prices) if prices else 20
    max_price = max(prices) if prices else 150

    market_stats = {
        "total_analyzed": len(parsed_ads),
        "min_price": min_price,
        "max_price": max_price,
        "median_price": median_price,
        "avg_price": avg_price,
        "updated_at": datetime.now().strftime("%d/%m/%Y à %H:%M:%S")
    }
    stats_file = os.path.join(DATA_DIR, "market_stats.json")
    with open(stats_file, "w", encoding="utf-8") as f:
        json.dump(market_stats, f, ensure_ascii=False, indent=2)

    print(f"Statistiques du marché : Min={min_price}€, Médiane={median_price}€, Moyenne={avg_price}€, Max={max_price}€")
    print("=== Pipeline d'extraction et notation terminé avec succès ===")
    return top_candidates, excluded_ads, market_stats

if __name__ == "__main__":
    run_extraction_and_ranking()
