import akshare as ak
import pandas as pd
import numpy as np
import ta
import yfinance as yf
import os
import requests

os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)
requests.session().proxies = {}

symbol = "014855"  # 沪深300ETF

# df = ak.fund_etf_hist_em(symbol=symbol)
df = yf.download("014855")  # 沪深300ETF（示例）
df = df.sort_values("日期")
df["close"] = df["收盘"]



df["ma20"] = df["close"].rolling(20).mean()
df["ma60"] = df["close"].rolling(60).mean()

df["rsi"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()

macd = ta.trend.MACD(df["close"])
df["macd"] = macd.macd()
df["signal"] = macd.macd_signal()

def trend_score(row):
    if row["ma20"] > row["ma60"] and row["macd"] > row["signal"]:
        return 1
    elif row["ma20"] > row["ma60"]:
        return 0.7
    elif row["ma20"] < row["ma60"]:
        return 0.3
    else:
        return 0.5

df["trend_score"] = df.apply(trend_score, axis=1)

def sentiment_score(rsi):
    if rsi < 40:
        return 1
    elif rsi < 70:
        return 0.5
    else:
        return 0

df["sentiment_score"] = df["rsi"].apply(sentiment_score)

df["val_score"] = (
    (df["close"] - df["close"].rolling(250).min()) /
    (df["close"].rolling(250).max() - df["close"].rolling(250).min())
)

df["val_score"] = 1 - df["val_score"]  # 越低估越高分

df["capital_score"] = np.where(df["close"].pct_change(3) > 0, 0.7, 0.4)

df["score"] = (
    0.4 * df["trend_score"] +
    0.25 * df["val_score"] +
    0.25 * df["capital_score"] +
    0.1 * df["sentiment_score"]
)

def signal(score):
    if score >= 0.75:
        return "强买"
    elif score >= 0.6:
        return "买入"
    elif score >= 0.4:
        return "持有"
    else:
        return "卖出"

df["signal"] = df["score"].apply(signal)