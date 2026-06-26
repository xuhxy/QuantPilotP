from datetime import datetime, timedelta

from .cache import exists, load, save
from .akshare_client import fetch_etf


CACHE_EXPIRE_DAYS = 1


def get_etf(symbol: str, force=False):
    """
    ⭐唯一入口：策略只调用这个
    """

    # 1. 强制刷新
    if force:
        df = fetch_etf(symbol)
        save(symbol, df)
        return df

    # 2. 没缓存
    if not exists(symbol):
        df = fetch_etf(symbol)
        save(symbol, df)
        return df

    df = load(symbol)

    # 3. 判断是否过期
    try:
        last_day = df["日期"].max()
        last_day = datetime.strptime(str(last_day), "%Y-%m-%d")

        if datetime.now() - last_day > timedelta(days=CACHE_EXPIRE_DAYS):
            print("缓存过期，更新数据...")
            df = fetch_etf(symbol)
            save(symbol, df)

    except:
        # 缓存坏了就重建
        df = fetch_etf(symbol)
        save(symbol, df)

    return df