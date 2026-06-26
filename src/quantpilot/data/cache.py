from pathlib import Path
import pandas as pd

CACHE_DIR = Path("src/quantpilot/cache/etf")
CACHE_DIR.mkdir(parents=True, exist_ok=True)


def path(symbol: str):
    return CACHE_DIR / f"{symbol}.parquet"


def exists(symbol: str) -> bool:
    return path(symbol).exists()


def load(symbol: str):
    return pd.read_parquet(path(symbol))


def save(symbol: str, df: pd.DataFrame):
    df.to_parquet(path(symbol), index=False)