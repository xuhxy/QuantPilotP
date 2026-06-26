from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT / "data"
REPORT_DIR = ROOT / "reports"
DB_DIR = ROOT / "database"
CACHE_DIR = ROOT / "data" / "cache"

for path in [DATA_DIR, REPORT_DIR, DB_DIR, CACHE_DIR]:
    path.mkdir(parents=True, exist_ok=True)