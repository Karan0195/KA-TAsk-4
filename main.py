#!/usr/bin/env python3
"""
==============================================================
RECRUITMENT & PLACEMENT MANAGEMENT SYSTEM (RPMS)
Student Project Implementation
Python + MySQL Architecture
==============================================================
"""

import sys
from pathlib import Path

# Ensure project root is in sys.path
_project_dir = Path(__file__).resolve().parent
if str(_project_dir) not in sys.path:
    sys.path.insert(0, str(_project_dir))

from rpms.app.menu import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Exiting...")
        sys.exit(0)
