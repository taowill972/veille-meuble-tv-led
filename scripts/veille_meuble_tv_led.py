# -*- coding: utf-8 -*-
"""
veille_meuble_tv_led.py
Master Runner pour le cycle de veille automatisé Meuble TV à LED
1. Scraping & Scoring Cognitif (/100) Leboncoin
2. Génération du classeur Excel 3 feuilles
3. Génération du Dashboard Apple OS/iOS autonome
4. Synchronisation Git vers taowill972/veille-meuble-tv-led
"""

import os
import sys
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from fetch_and_rank_led_tv import run_extraction_and_ranking
from build_excel_report import create_excel_report
from build_apple_dashboard import generate_dashboard
from git_sync import run_git_sync

def run_full_cycle():
    print("=================================================================")
    print("🚀 [CYCLE VEILLE AUTOMATISÉE] MEUBLE TV À LED (ATHIS-MONS 2026)")
    print("=================================================================")
    
    # 1. Scraping, scoring & photos Base64
    run_extraction_and_ranking()
    
    # 2. Excel
    create_excel_report()
    
    # 3. Apple Dashboard
    generate_dashboard()
    
    # 4. Git Push
    run_git_sync()
    
    print("\n✅ Cycle complet Meuble TV à LED exécuté avec succès.")

if __name__ == "__main__":
    run_full_cycle()
