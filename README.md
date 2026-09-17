# 🛋️ Veille, Audit & Dashboard : Meuble TV à LED Intégré

Système automatisé de surveillance, scoring multi-critères (/100) et restitution décisionnelle pour les **meubles TV avec éclairage LED intégré** sur Leboncoin (Athis-Mons 91200 et rayon 25 km).

Projet rattaché à la **Suite Décisionnelle IMMO ATHIS 2026** (Équipement Salon, TV OLED 55" & logistique Renault Scénic III).

---

## 🌟 Points Forts & Spécifications

- **Données 100% Réelles & Vérifiées :** Zéro mock, zéro simulation générique (Directive Mode X - Sincérité Technique Absolue).
- **Dashboard Autonome Apple OS/iOS Signature :**
  - Design épuré Cupertino Glassmorphism (Thème double : Gris Chaud Texturé + Mode Sombre Obsidian).
  - Photos des meubles encodées en **Base64** haute définition pour une portabilité totale sans serveur web ni liens cassés.
  - Filtres instantanés par *Segmented Controls* : *Tous, Télécommande RGB, Blanc Laqué, Scénic III (≤ 140cm), Moins de 50 €*.
  - Jauges d'Argus dynamiques avec repères Médiane, Moyenne et curseur `🎯 Annonce : XX € ▼`.
  - Fiche modale d'inspection rapide (*Quick Look iOS*) avec carrousel d'images HD et descriptif complet.
- **Classeur Excel Professionnel (.xlsx) à 3 Feuilles :**
  1. `TOP Classement LED` : Hiérarchie détaillée avec liens cliquables et mise en forme conditionnelle.
  2. `Grille de Notation (100 pts)` : Barème complet des 5 piliers de scoring.
  3. `Modèles Exclus & Justifications` : Traçabilité des annonces éliminées (pas de LED, faux mots-clés, hors budget).

---

## 🎯 Grille de Scoring Cognitif /100

| Pilier d'Évaluation | Pts Max | Critères & Conditions |
| :--- | :---: | :--- |
| **1. Système LED & Contrôle** | 25 | Ruban RGB avec télécommande (+25), clips LED verre trempé (+20), ruban intégré (+18). |
| **2. Rapport Qualité/Prix & Cote d'Occasion** | 25 | Prix ≤ 45€ (+25), 46-75€ (+22), 76-100€ (+18), > 100€ (+10-14). Économie vs MSRP. |
| **3. Format Scénic III & TV 55"** | 20 | Longueur 120-140 cm direct (+15), 141-160 cm (+11). Proximité ≤ 15 km (+5). |
| **4. Rangements Multimédia** | 15 | Niches ouvertes Box/PS5 + portes/tiroirs fermés (+15). Dissimulation des câbles. |
| **5. Finition & État Visuel HD** | 15 | Blanc laqué brillant High Gloss (+15), bi-matière bois/blanc (+14), noir laqué (+13). |

---

## 📁 Organisation du Dépôt

```
MEUBLE-TV-LED/
├── index.html                                    # Dashboard Apple OS/iOS 100% autonome (Base64)
├── Classement_Meuble_TV_LED_AthisMons_2026.xlsx  # Classeur Excel professionnel 3 feuilles
├── README.md                                     # Documentation officielle
├── audit_result.md                               # Rapport d'audit de conformité /auto-test
├── data/
│   ├── meuble_tv_led_raw_ads.json                # Annonces brutes Leboncoin extraites
│   ├── meuble_tv_led_listings.json               # Annonces qualifiées, notées et classées
│   ├── meuble_tv_led_excluded.json               # Annonces écartées avec justifications
│   └── market_stats.json                         # Médiane, moyenne, min et max du marché
├── photos/                                       # Photos HD téléchargées
└── scripts/
    ├── fetch_and_rank_led_tv.py                  # Scraper & scoring cognitif
    ├── build_excel_report.py                     # Générateur de l'Excel 3 feuilles
    ├── build_apple_dashboard.py                  # Générateur du dashboard HTML Cupertino
    ├── git_sync.py                               # Synchronisation automatique GitHub
    └── veille_meuble_tv_led.py                   # Master runner du cycle
```

---

## 🚀 Utilisation & Commandes

Exécuter un cycle complet de veille, scoring, génération de l'Excel et du dashboard :

```bash
python scripts/veille_meuble_tv_led.py
```

Synchroniser les mises à jour avec le dépôt GitHub :

```bash
python scripts/git_sync.py
```
