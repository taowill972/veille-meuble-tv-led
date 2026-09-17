#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
git_sync.py - Cross-platform Git Synchronization pour Veille Meuble TV LED
"""

import os
import subprocess
from datetime import datetime, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(SCRIPT_DIR)

def run_git_sync():
    print(f"=== [Git Sync Meuble TV LED] Démarrage synchronisation {datetime.now(timezone.utc).isoformat()} ===")
    try:
        # Fetch & merge remote changes
        subprocess.run(["git", "fetch", "origin", "main"], cwd=REPO_DIR, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["git", "merge", "origin/main", "--no-edit"], cwd=REPO_DIR, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Stage all updated files
        subprocess.run(["git", "add", "-A"], cwd=REPO_DIR, check=True)

        # Check if there are changes to commit
        diff_res = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO_DIR)
        if diff_res.returncode != 0:
            msg = f"Auto-Veille Meuble TV LED [{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}] Sync dashboard, data & report"
            subprocess.run(["git", "commit", "-m", msg], cwd=REPO_DIR, check=True)
            subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR, check=True)
            print(f"[Git Sync] Pushed changes successfully: {msg}")
        else:
            print("[Git Sync] Working tree clean, nothing to commit.")
        return True
    except Exception as e:
        print(f"[Git Sync] Warning: {e}")
        return False

if __name__ == "__main__":
    run_git_sync()
