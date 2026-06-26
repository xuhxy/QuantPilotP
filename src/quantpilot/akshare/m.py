import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

def normalize_akshare(df):
    # 自动找日期列
    date_col = [c for c in df.columns if "date" in c.lower() or "日期" in c][0]
    df[date_col] = pd.to_datetime(df[date_col])

    df = df.sort_values(date_col)
    df = df.set_index(date_col)

    return df

# =========================
# 1️⃣ 获取上证指数数据
# =========================
df = ak.stock_zh_index_daily(symbol="sh000001")

# 股票 贵州茅台
# df = ak.stock_zh_a_hist(
#     symbol="600519",
#     period="daily",
#     start_date="20200101",
#     adjust="qfq"
# )

# 
# df = ak.fund_etf_hist_em(symbol="510300")
df = normalize_akshare(df)

# =========================
# 2️⃣ 数据处理
# =========================
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")
df.set_index("date", inplace=True)

# =========================
# 3️⃣ 画图
# =========================
plt.figure(figsize=(12, 6))

df["close"].plot(label="上证指数")

plt.title("上证指数历史走势（AkShare）")
plt.xlabel("Date")
plt.ylabel("Close Price")

plt.grid(True)
plt.legend()

plt.show()