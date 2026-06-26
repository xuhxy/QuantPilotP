import time
import random
import akshare as ak


def fetch_etf(symbol: str):
    """
    从AkShare获取ETF数据（带重试+降频）
    """

    for i in range(5):
        try:
            # ⭐防止被封（关键）
            time.sleep(random.uniform(2, 5))

            df = ak.fund_etf_hist_em(symbol=symbol)

            return df

        except Exception as e:
            print(f"[AkShare失败 {i+1}/5] {e}")
            time.sleep(3)

    raise RuntimeError("AkShare连续失败")