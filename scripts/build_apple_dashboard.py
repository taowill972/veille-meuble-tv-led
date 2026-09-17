# -*- coding: utf-8 -*-
"""
build_apple_dashboard.py
Génère le Dashboard Apple OS/iOS Signature 100% autonome
avec photos Base64, design Cupertino Glassmorphism, jauges d'argus dynamiques,
filtres interactifs et modal Quick Look.
"""

import os
import json

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(CURRENT_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_HTML = os.path.join(BASE_DIR, "index.html")

def generate_dashboard():
    print("=== Génération du Dashboard Apple OS/iOS Meuble TV LED ===")
    
    listings_file = os.path.join(DATA_DIR, "meuble_tv_led_listings.json")
    stats_file = os.path.join(DATA_DIR, "market_stats.json")

    with open(listings_file, "r", encoding="utf-8") as f:
        listings = json.load(f)
    
    stats = {}
    if os.path.exists(stats_file):
        with open(stats_file, "r", encoding="utf-8") as f:
            stats = json.load(f)

    json_items = json.dumps(listings, ensure_ascii=False)
    median_val = stats.get("median_price", 75)
    avg_val = stats.get("avg_price", 75)
    total_analyzed = stats.get("total_analyzed", len(listings))

    html_content = f"""<!DOCTYPE html>
<html lang="fr" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meuble TV à LED Intégré · Signature Apple OS/iOS · IMMO ATHIS 2026</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://unpkg.com/lucide@latest"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['-apple-system', 'BlinkMacSystemFont', 'Inter', 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', 'sans-serif'],
          }},
          colors: {{
            apple: {{
              blue: '#007AFF',
              green: '#34C759',
              indigo: '#5856D6',
              orange: '#FF9500',
              pink: '#FF2D55',
              purple: '#AF52DE',
              red: '#FF3B30',
              teal: '#5AC8FA',
              yellow: '#FFCC00',
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    * {{ -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }}
    
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Inter", "SF Pro Display", sans-serif;
      background-color: #c5c0b7;
      background-image: 
        radial-gradient(at 15% 15%, rgba(208, 203, 194, 0.95) 0px, transparent 55%),
        radial-gradient(at 85% 85%, rgba(188, 182, 173, 0.90) 0px, transparent 55%),
        radial-gradient(at 50% 50%, rgba(200, 194, 185, 0.92) 0px, transparent 65%);
      background-attachment: fixed;
      color: #181716;
    }}
    .dark body, body.dark, html.dark body {{
      background-color: #090a0c !important;
      background-image: none !important;
      color: #f1f5f9 !important;
    }}
    
    .apple-glass {{
      background: rgba(238, 234, 227, 0.94);
      backdrop-filter: blur(28px) saturate(160%);
      -webkit-backdrop-filter: blur(28px) saturate(160%);
      border: 1px solid rgba(185, 178, 168, 0.75);
      box-shadow: 0 10px 30px -5px rgba(50, 45, 38, 0.10), inset 0 1px 0 0 rgba(255, 255, 255, 0.45);
    }}
    .dark .apple-glass {{
      background: rgba(24, 24, 27, 0.82) !important;
      backdrop-filter: blur(30px) saturate(190%) !important;
      -webkit-backdrop-filter: blur(30px) saturate(190%) !important;
      border: 1px solid rgba(255, 255, 255, 0.12) !important;
      box-shadow: 0 12px 35px -5px rgba(0, 0, 0, 0.5), inset 0 1px 0 0 rgba(255, 255, 255, 0.12) !important;
    }}

    .apple-btn {{
      transition: transform 0.18s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.18s ease;
    }}
    .apple-btn:active {{
      transform: scale(0.96);
    }}

    .segmented-pill {{
      padding: 0.4rem 0.9rem;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 600;
      transition: all 0.2s ease;
      background: transparent;
      color: #64748b;
      border: 1px solid transparent;
      cursor: pointer;
    }}
    .dark .segmented-pill {{
      color: #94a3b8;
    }}
    .segmented-pill:hover {{
      color: #0f172a;
      background: rgba(0, 0, 0, 0.05);
    }}
    .dark .segmented-pill:hover {{
      color: #ffffff;
      background: rgba(255, 255, 255, 0.08);
    }}
    .segmented-pill.active {{
      background: #007AFF !important;
      color: #ffffff !important;
      box-shadow: 0 2px 8px rgba(0, 122, 255, 0.35);
    }}
    
    /* Animation pulsation lueur LED */
    @keyframes led-glow {{
      0%, 100% {{ box-shadow: 0 0 15px rgba(0, 122, 255, 0.3); }}
      50% {{ box-shadow: 0 0 25px rgba(175, 82, 222, 0.5); }}
    }}
    .led-border {{
      animation: led-glow 4s ease-in-out infinite;
    }}
  </style>
</head>
<body class="min-h-screen transition-colors duration-300 pb-20">

  <!-- TOP HEADER -->
  <header class="sticky top-0 z-40 border-b border-black/10 bg-[#ded9d0]/90 dark:bg-[#121214]/85 backdrop-blur-2xl transition-colors duration-300">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <a href="../index.html" title="Retour au Hub IMMO ATHIS" class="w-9 h-9 rounded-xl bg-gradient-to-tr from-purple-600 to-blue-500 flex items-center justify-center text-white font-bold shadow-md shadow-purple-500/25 apple-btn hover:opacity-90">
          <i data-lucide="sparkles" class="w-5 h-5"></i>
        </a>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="text-base font-bold tracking-tight text-slate-900 dark:text-white">Meuble TV à LED Intégré</h1>
            <span class="text-[10px] font-extrabold uppercase px-2 py-0.5 rounded-full bg-purple-500/15 text-purple-600 dark:text-purple-400 border border-purple-500/25">
              Veille Spécifique LED 2026
            </span>
          </div>
          <p class="text-xs text-slate-600 dark:text-slate-400 font-medium">Bandeau RGB · Étagères Verre · Finitions Laquées · Scénic III (≤ 140cm)</p>
        </div>
      </div>

      <div class="flex items-center gap-2.5">
        <a href="Classement_Meuble_TV_LED_AthisMons_2026.xlsx" download title="Télécharger le classeur Excel 3 feuilles" class="px-3.5 py-1.5 rounded-full flex items-center gap-1.5 text-xs font-bold text-white bg-emerald-600 hover:bg-emerald-700 shadow-sm shadow-emerald-500/25 apple-btn">
          <i data-lucide="file-spreadsheet" class="w-3.5 h-3.5"></i>
          <span>Excel .xlsx</span>
        </a>

        <a href="../index.html" title="Retour à la Suite Décisionnelle IMMO ATHIS" class="px-3 py-1.5 rounded-full flex items-center gap-1.5 text-xs font-semibold text-slate-700 dark:text-slate-200 bg-black/5 dark:bg-white/10 hover:bg-black/10 dark:hover:bg-white/15 apple-btn">
          <i data-lucide="layout-grid" class="w-3.5 h-3.5"></i>
          <span class="hidden sm:inline">Hub Central</span>
        </a>

        <button onclick="toggleTheme()" class="w-9 h-9 rounded-full flex items-center justify-center text-slate-600 dark:text-slate-300 bg-black/5 dark:bg-white/10 hover:bg-black/10 dark:hover:bg-white/15 apple-btn">
          <i data-lucide="moon" id="theme-moon" class="w-4 h-4 hidden dark:block"></i>
          <i data-lucide="sun" id="theme-sun" class="w-4 h-4 block dark:hidden"></i>
        </button>
      </div>
    </div>
  </header>

  <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 space-y-6">

    <!-- HERO / LIVE AUTOMATION BAR -->
    <div class="apple-glass rounded-3xl p-5 relative overflow-hidden led-border">
      <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        
        <div class="flex items-center gap-3.5">
          <div class="w-12 h-12 rounded-2xl bg-gradient-to-tr from-purple-500 to-indigo-600 flex items-center justify-center text-white text-2xl shadow-lg shadow-purple-500/30 flex-shrink-0">
            🛋️
          </div>
          <div>
            <div class="flex items-center gap-2 flex-wrap">
              <span class="text-sm font-black uppercase tracking-wider text-slate-900 dark:text-white">Audit Cognitif & Veille Leboncoin : Meubles TV LED</span>
              <span class="text-[10px] font-bold uppercase px-2 py-0.5 rounded-full bg-emerald-500/15 text-emerald-600 dark:text-emerald-400 border border-emerald-500/25">
                100% Vérifié & Photos Base64
              </span>
            </div>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 flex items-center gap-2 flex-wrap">
              <i data-lucide="map-pin" class="w-3.5 h-3.5 text-[#007AFF]"></i>
              <span>Athis-Mons (91200) + Rayon 25 km</span>
              <span class="text-slate-300 dark:text-slate-600">·</span>
              <span>{total_analyzed} annonces analysées</span>
              <span class="text-slate-300 dark:text-slate-600">·</span>
              <span>Médiane : <strong>{median_val} €</strong> · Moyenne : <strong>{avg_val} €</strong></span>
            </p>
          </div>
        </div>

        <div class="flex items-center gap-3 self-start md:self-auto bg-black/5 dark:bg-white/5 p-2.5 px-4 rounded-2xl border border-black/5 dark:border-white/5">
          <i data-lucide="clock" class="w-4 h-4 text-purple-500"></i>
          <div>
            <div class="text-[10px] font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Cycle 8h Veille Active dans</div>
            <div class="font-mono font-black text-sm text-purple-600 dark:text-purple-400 tracking-tight" id="countdown-timer">--:--:--</div>
          </div>
        </div>

      </div>
    </div>

    <!-- FILTER SEGMENTED CONTROLS -->
    <div class="flex flex-wrap items-center justify-between gap-3 pt-2">
      <div class="flex flex-wrap items-center gap-1.5 bg-black/5 dark:bg-white/5 p-1 rounded-full border border-black/5 dark:border-white/5" id="filter-bar">
        <button class="segmented-pill active" onclick="setFilter('all', this)">
          <span>Tous les Meubles LED</span>
          <span class="ml-1 px-1.5 py-0.2 rounded-full text-[10px] bg-white/20">{len(listings)}</span>
        </button>
        <button class="segmented-pill" onclick="setFilter('rgb', this)">
          <i data-lucide="gamepad-2" class="w-3 h-3 inline mr-1 text-pink-400"></i>
          <span>Télécommande RGB</span>
        </button>
        <button class="segmented-pill" onclick="setFilter('laque', this)">
          <i data-lucide="sparkle" class="w-3 h-3 inline mr-1 text-amber-400"></i>
          <span>Blanc Laqué</span>
        </button>
        <button class="segmented-pill" onclick="setFilter('scenic', this)">
          <i data-lucide="car" class="w-3 h-3 inline mr-1 text-emerald-400"></i>
          <span>Format Scénic III (≤ 140cm)</span>
        </button>
        <button class="segmented-pill" onclick="setFilter('budget', this)">
          <i data-lucide="tag" class="w-3 h-3 inline mr-1 text-blue-400"></i>
          <span>Moins de 50 €</span>
        </button>
      </div>

      <div class="text-xs text-slate-500 dark:text-slate-400 font-medium">
        Affichage de <span id="visible-count" class="font-bold text-slate-900 dark:text-white">{len(listings)}</span> opportunités qualifiées
      </div>
    </div>

    <!-- GRID CARDS -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="cards-grid">
"""

    for it in listings:
        rank = it.get("rank", 1)
        score = it.get("score", 90)
        price = it.get("price", 0)
        city = it.get("city", "Île-de-France")
        dist = it.get("dist", 0)
        title = it.get("title", "")
        img_b64 = it.get("main_image_b64", "")
        led_type = it.get("led_type", "LED intégrée")
        remote_status = it.get("remote_status", "Standard")
        scenic_status = it.get("scenic_status", "")
        dim_str = it.get("dimensions_str", "")
        finish_name = it.get("finish_name", "")
        storage_desc = it.get("storage_desc", "")
        bargain_gauge = it.get("bargain_gauge", "🟢 🟢 🟢 ⚪")
        bargain_level = it.get("bargain_level", "Bonne affaire")
        discount = it.get("discount", 0)
        msrp = it.get("msrp", 240)
        url = it.get("url", "")
        item_id = it.get("id", "")

        is_rgb = "télécommande" in remote_status.lower() or "rgb" in led_type.lower()
        is_laque = "laqué" in finish_name.lower() or "laque" in title.lower()
        is_scenic = it.get("length_cm", 130) <= 140
        is_budget = price <= 50

        # Données d'attribut pour le filtre JS
        data_tags = []
        if is_rgb: data_tags.append("rgb")
        if is_laque: data_tags.append("laque")
        if is_scenic: data_tags.append("scenic")
        if is_budget: data_tags.append("budget")
        data_tags_str = " ".join(data_tags)

        # Calcul curseur jauge Argus (échelle 20€ à 150€)
        scale_min = 20
        scale_max = 150
        pct_price = max(5, min(95, round(((price - scale_min) / (scale_max - scale_min)) * 100)))
        pct_median = max(5, min(95, round(((median_val - scale_min) / (scale_max - scale_min)) * 100)))

        rank_badge_class = "from-amber-400 to-amber-600 text-white shadow-amber-500/30" if rank == 1 else "from-blue-600 to-indigo-600 text-white shadow-blue-500/25"
        rank_text = f"👑 #1 PÉPITE LED" if rank == 1 else f"#{rank} TOP SÉLECTION"

        html_content += f"""
      <!-- CARD ITEM {rank} -->
      <div class="apple-glass rounded-3xl overflow-hidden flex flex-col justify-between hover:shadow-2xl transition-all duration-300 group border border-black/5 dark:border-white/10" data-tags="{data_tags_str}" data-price="{price}" data-id="{item_id}">
        
        <!-- IMAGE & BADGES -->
        <div class="relative aspect-[16/10] bg-black/10 dark:bg-black/40 overflow-hidden">
          <img src="{img_b64}" alt="{title}" class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500" loading="lazy" />
          
          <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-black/20 pointer-events-none"></div>
          
          <!-- Top Badges -->
          <div class="absolute top-3 left-3 flex items-center gap-2">
            <span class="px-2.5 py-1 rounded-full text-[11px] font-black tracking-wide uppercase bg-gradient-to-r {rank_badge_class} shadow-md">
              {rank_text}
            </span>
            <span class="px-2.5 py-1 rounded-full text-[11px] font-extrabold bg-black/60 backdrop-blur-md text-white border border-white/15">
              Score {score}/100
            </span>
          </div>

          <!-- Price Tag Bottom Left -->
          <div class="absolute bottom-3 left-3">
            <div class="flex items-baseline gap-1.5">
              <span class="text-2xl font-black text-white drop-shadow-md">{price} €</span>
              <span class="text-xs font-semibold text-emerald-400 drop-shadow-sm">(-{discount}% vs neuf)</span>
            </div>
            <div class="text-[10px] text-white/80 font-medium">MSRP Neuf estimé : ~{msrp} €</div>
          </div>

          <!-- City Tag Bottom Right -->
          <div class="absolute bottom-3 right-3 text-right">
            <div class="text-xs font-bold text-white flex items-center gap-1 drop-shadow-md">
              <i data-lucide="map-pin" class="w-3 h-3 text-[#007AFF]"></i>
              <span>{city}</span>
            </div>
            <div class="text-[10px] text-white/80 font-medium">{dist} km d'Athis-Mons</div>
          </div>
        </div>

        <!-- CONTENT BODY -->
        <div class="p-5 space-y-4 flex-1 flex flex-col justify-between">
          
          <div class="space-y-3">
            <h3 class="font-bold text-sm text-slate-900 dark:text-white line-clamp-2 leading-snug" title="{title}">
              {title}
            </h3>

            <!-- CARACTÉRISTIQUES CLÉS -->
            <div class="space-y-1.5 text-xs text-slate-600 dark:text-slate-300">
              
              <div class="flex items-start gap-2 py-1 border-b border-black/5 dark:border-white/5">
                <i data-lucide="zap" class="w-3.5 h-3.5 text-purple-500 mt-0.5 flex-shrink-0"></i>
                <div>
                  <span class="text-slate-400">Éclairage :</span>
                  <strong class="text-slate-900 dark:text-white ml-1 font-semibold">{led_type}</strong>
                </div>
              </div>

              <div class="flex items-start gap-2 py-1 border-b border-black/5 dark:border-white/5">
                <i data-lucide="sliders" class="w-3.5 h-3.5 text-blue-500 mt-0.5 flex-shrink-0"></i>
                <div>
                  <span class="text-slate-400">Contrôle :</span>
                  <strong class="text-slate-900 dark:text-white ml-1 font-semibold">{remote_status}</strong>
                </div>
              </div>

              <div class="flex items-start gap-2 py-1 border-b border-black/5 dark:border-white/5">
                <i data-lucide="maximize" class="w-3.5 h-3.5 text-emerald-500 mt-0.5 flex-shrink-0"></i>
                <div>
                  <span class="text-slate-400">Dimensions :</span>
                  <strong class="text-slate-900 dark:text-white ml-1 font-semibold">{dim_str}</strong>
                </div>
              </div>

              <div class="flex items-start gap-2 py-1 border-b border-black/5 dark:border-white/5">
                <i data-lucide="palette" class="w-3.5 h-3.5 text-pink-500 mt-0.5 flex-shrink-0"></i>
                <div>
                  <span class="text-slate-400">Finition :</span>
                  <strong class="text-slate-900 dark:text-white ml-1 font-semibold">{finish_name}</strong>
                </div>
              </div>

              <div class="flex items-start gap-2 py-1">
                <i data-lucide="car" class="w-3.5 h-3.5 text-amber-500 mt-0.5 flex-shrink-0"></i>
                <div>
                  <span class="text-slate-400">Scénic III :</span>
                  <strong class="text-slate-900 dark:text-white ml-1 font-semibold">{scenic_status}</strong>
                </div>
              </div>

            </div>

            <!-- JAUGE GRAPHIQUE D'ARGUS OCCASION -->
            <div class="rounded-2xl p-3 bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 space-y-2">
              <div class="flex items-center justify-between text-[11px]">
                <span class="font-bold text-slate-800 dark:text-slate-200">Jauge Argus & Marché</span>
                <span class="font-extrabold text-xs text-emerald-600 dark:text-emerald-400">{bargain_level}</span>
              </div>
              
              <!-- Barre spectre -->
              <div class="relative h-2.5 rounded-full bg-gradient-to-r from-emerald-500 via-blue-500 via-amber-500 to-rose-500 overflow-visible mt-3 mb-4">
                <!-- Repère Médiane -->
                <div class="absolute -top-1 bottom-0 w-0.5 bg-white shadow-sm" style="left: {pct_median}%;" title="Médiane : {median_val}€">
                  <span class="absolute -top-4 -translate-x-1/2 text-[9px] font-bold text-slate-400">Médiane {median_val}€</span>
                </div>
                <!-- Curseur Annonce -->
                <div class="absolute -top-2 w-3.5 h-3.5 rounded-full bg-white border-2 border-purple-600 shadow-md transform -translate-x-1/2 cursor-pointer" style="left: {pct_price}%;" title="Cette annonce : {price}€">
                  <span class="absolute -bottom-5 -translate-x-1/2 whitespace-nowrap text-[9px] font-black text-purple-600 dark:text-purple-400 bg-purple-100 dark:bg-purple-900/60 px-1 rounded">🎯 {price}€</span>
                </div>
              </div>

              <div class="flex items-center justify-between text-[10px] text-slate-500 dark:text-slate-400 pt-1">
                <span>Min: 20 €</span>
                <span>Écart Médiane: <strong class="text-emerald-600 dark:text-emerald-400">{price - median_val:+d} €</strong></span>
                <span>Max: 150 €</span>
              </div>
            </div>

          </div>

          <!-- ACTIONS BOTTOM -->
          <div class="grid grid-cols-2 gap-2 pt-3 border-t border-black/5 dark:border-white/5">
            <button onclick="openQuickLook('{item_id}')" class="py-2.5 rounded-full text-xs font-semibold text-slate-700 dark:text-slate-200 bg-black/5 dark:bg-white/10 hover:bg-black/10 dark:hover:bg-white/15 apple-btn flex items-center justify-center gap-1.5">
              <i data-lucide="eye" class="w-3.5 h-3.5"></i>
              <span>Coup d'œil</span>
            </button>

            <a href="{url}" target="_blank" rel="noopener noreferrer" class="py-2.5 rounded-full text-xs font-bold text-white bg-[#007AFF] hover:bg-blue-600 shadow-sm shadow-blue-500/25 apple-btn flex items-center justify-center gap-1.5">
              <span>Leboncoin</span>
              <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
            </a>
          </div>

        </div>

      </div>
"""

    html_content += f"""
    </div>

  </main>

  <!-- QUICK LOOK MODAL SHEET (iOS Style) -->
  <div id="quick-look-modal" class="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 opacity-0 pointer-events-none transition-opacity duration-300">
    <div class="absolute inset-0 bg-black/70 backdrop-blur-md" onclick="closeQuickLook()"></div>
    
    <div class="relative apple-glass w-full max-w-2xl max-h-[90vh] rounded-3xl overflow-hidden flex flex-col shadow-2xl z-10 transform scale-95 transition-transform duration-300" id="modal-container">
      
      <!-- Modal Header -->
      <div class="p-4 sm:p-5 border-b border-black/10 dark:border-white/10 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="w-2.5 h-2.5 rounded-full bg-purple-500 animate-pulse"></span>
          <h2 class="text-sm font-bold text-slate-900 dark:text-white" id="modal-title">Détails de l'opportunité</h2>
        </div>
        <button onclick="closeQuickLook()" class="w-8 h-8 rounded-full flex items-center justify-center text-slate-400 hover:text-slate-200 bg-black/5 dark:bg-white/10 apple-btn">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <!-- Modal Body -->
      <div class="p-5 sm:p-6 overflow-y-auto space-y-5 flex-1">
        
        <!-- Image Slider / Gallery -->
        <div class="relative aspect-video rounded-2xl overflow-hidden bg-black/20">
          <img id="modal-img" src="" alt="" class="w-full h-full object-contain" />
          <div class="absolute bottom-2 right-2 flex gap-1.5" id="modal-thumbnails"></div>
        </div>

        <!-- Specs Grid -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 text-center">
          <div class="p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5">
            <div class="text-[10px] text-slate-400 uppercase font-bold">Prix Demandé</div>
            <div class="text-lg font-black text-slate-900 dark:text-white mt-0.5" id="modal-price">-- €</div>
          </div>
          <div class="p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5">
            <div class="text-[10px] text-slate-400 uppercase font-bold">Score Global</div>
            <div class="text-lg font-black text-[#007AFF] mt-0.5" id="modal-score">--/100</div>
          </div>
          <div class="p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5">
            <div class="text-[10px] text-slate-400 uppercase font-bold">Distance</div>
            <div class="text-lg font-black text-emerald-500 mt-0.5" id="modal-dist">-- km</div>
          </div>
          <div class="p-3 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5">
            <div class="text-[10px] text-slate-400 uppercase font-bold">Scénic III</div>
            <div class="text-xs font-bold text-slate-900 dark:text-white mt-1.5" id="modal-scenic">--</div>
          </div>
        </div>

        <!-- Full Description -->
        <div class="space-y-2">
          <h4 class="text-xs font-bold uppercase text-slate-400 tracking-wider">Descriptif Vendeur & Audit IA</h4>
          <div class="p-4 rounded-2xl bg-black/5 dark:bg-white/5 border border-black/5 dark:border-white/5 text-xs text-slate-700 dark:text-slate-300 leading-relaxed max-h-48 overflow-y-auto whitespace-pre-line" id="modal-desc">
            --
          </div>
        </div>

      </div>

      <!-- Modal Footer -->
      <div class="p-4 border-t border-black/10 dark:border-white/10 flex items-center justify-between gap-3 bg-black/5 dark:bg-white/5">
        <div class="text-xs text-slate-500 dark:text-slate-400 font-medium" id="modal-city">
          --
        </div>
        <a id="modal-lbc-link" href="#" target="_blank" rel="noopener noreferrer" class="px-5 py-2.5 rounded-full text-xs font-bold text-white bg-[#007AFF] hover:bg-blue-600 shadow-md shadow-blue-500/25 apple-btn flex items-center gap-1.5">
          <span>Ouvrir l'annonce Leboncoin</span>
          <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
        </a>
      </div>

    </div>
  </div>

  <script>
    const itemsData = {json_items};
    const itemsMap = {{}};
    itemsData.forEach(it => itemsMap[it.id] = it);

    // Initialisation icônes Lucide
    lucide.createIcons();

    // Gestion du Thème
    function toggleTheme() {{
      const html = document.documentElement;
      if (html.classList.contains('dark')) {{
        html.classList.remove('dark');
        localStorage.theme = 'light';
      }} else {{
        html.classList.add('dark');
        localStorage.theme = 'dark';
      }}
    }}
    if (localStorage.theme === 'light' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: light)').matches)) {{
      document.documentElement.classList.remove('dark');
    }} else {{
      document.documentElement.classList.add('dark');
    }}

    // Filtrage dynamique
    function setFilter(tag, btn) {{
      document.querySelectorAll('#filter-bar button').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const cards = document.querySelectorAll('#cards-grid > div');
      let visible = 0;

      cards.forEach(c => {{
        const tags = c.getAttribute('data-tags') || '';
        const price = parseFloat(c.getAttribute('data-price') || '0');

        let show = false;
        if (tag === 'all') {{
          show = true;
        }} else if (tag === 'rgb' && tags.includes('rgb')) {{
          show = true;
        }} else if (tag === 'laque' && tags.includes('laque')) {{
          show = true;
        }} else if (tag === 'scenic' && tags.includes('scenic')) {{
          show = true;
        }} else if (tag === 'budget' && price <= 50) {{
          show = true;
        }}

        if (show) {{
          c.style.display = 'flex';
          visible++;
        }} else {{
          c.style.display = 'none';
        }}
      }});

      document.getElementById('visible-count').textContent = visible;
    }}

    // Quick Look Modal
    function openQuickLook(id) {{
      const it = itemsMap[id];
      if (!it) return;

      document.getElementById('modal-title').textContent = it.title;
      document.getElementById('modal-price').textContent = it.price + ' €';
      document.getElementById('modal-score').textContent = it.score + '/100';
      document.getElementById('modal-dist').textContent = (it.dist || '--') + ' km';
      document.getElementById('modal-scenic').textContent = it.scenic_status || 'Conforme';
      document.getElementById('modal-desc').textContent = it.body || 'Aucun descriptif textuel fourni.';
      document.getElementById('modal-city').textContent = (it.city || '') + ' (' + (it.zipcode || '') + ')';
      document.getElementById('modal-lbc-link').href = it.url;

      const mainImg = document.getElementById('modal-img');
      const thumbs = document.getElementById('modal-thumbnails');
      thumbs.innerHTML = '';

      const imgs = it.b64_images && it.b64_images.length > 0 ? it.b64_images : [it.main_image_b64];
      mainImg.src = imgs[0] || '';

      if (imgs.length > 1) {{
        imgs.forEach((imgSrc, idx) => {{
          const b = document.createElement('button');
          b.className = 'w-7 h-7 rounded-lg overflow-hidden border border-white/40 shadow-sm transition-transform hover:scale-110';
          b.innerHTML = `<img src="${{imgSrc}}" class="w-full h-full object-cover"/>`;
          b.onclick = () => {{ mainImg.src = imgSrc; }};
          thumbs.appendChild(b);
        }});
      }}

      const modal = document.getElementById('quick-look-modal');
      const container = document.getElementById('modal-container');
      modal.classList.remove('opacity-0', 'pointer-events-none');
      container.classList.remove('scale-95');
      container.classList.add('scale-100');
    }}

    function closeQuickLook() {{
      const modal = document.getElementById('quick-look-modal');
      const container = document.getElementById('modal-container');
      modal.classList.add('opacity-0', 'pointer-events-none');
      container.classList.remove('scale-100');
      container.classList.add('scale-95');
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') closeQuickLook();
    }});

    // Compte à rebours 8h (04:00, 12:00, 20:00)
    function updateCountdown() {{
      const now = new Date();
      const h = now.getHours();
      const m = now.getMinutes();
      const s = now.getSeconds();

      const targets = [
        new Date(now.getFullYear(), now.getMonth(), now.getDate(), 4, 0, 0),
        new Date(now.getFullYear(), now.getMonth(), now.getDate(), 12, 0, 0),
        new Date(now.getFullYear(), now.getMonth(), now.getDate(), 20, 0, 0),
        new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1, 4, 0, 0),
      ];

      let nextTarget = targets[0];
      for (let t of targets) {{
        if (t > now) {{
          nextTarget = t;
          break;
        }}
      }}

      const diffMs = nextTarget - now;
      const diffHrs = Math.floor(diffMs / (1000 * 60 * 60));
      const diffMins = Math.floor((diffMs % (1000 * 60 * 60)) / (1000 * 60));
      const diffSecs = Math.floor((diffMs % (1000 * 60)) / 1000);

      const fmt = (v) => String(v).padStart(2, '0');
      document.getElementById('countdown-timer').textContent = `${{fmt(diffHrs)}}:${{fmt(diffMins)}}:${{fmt(diffSecs)}}`;
    }}
    setInterval(updateCountdown, 1000);
    updateCountdown();
  </script>
</body>
</html>
"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Dashboard Apple OS/iOS Meuble TV LED généré avec succès : {OUTPUT_HTML}")
    return OUTPUT_HTML

if __name__ == "__main__":
    generate_dashboard()
