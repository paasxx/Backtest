import yfinance as yf
from datetime import date, timedelta, datetime


assets = {
    "BTC": "BTC-USD",
    "ETH": "ETH-USD",
    "USDT": "USDT-USD",
    "USDC": "USDC-USD",
    "BNB": "BNB-USD",
    "BUSD": "BUSD-USD",
    "XRP": "XRP-USD",
    "ADA": "ADA-USD",
    "SOL": "SOL-USD",
    "DOGE": "DOGE-USD",
    "DOT": "DOT-USD",
    "HEX": "HEX-USD",
    "SHIB": "SHIB-USD",
    "DAI": "DAI-USD",
    "WTRX": "WTRX-USD",
    "AVAX": "AVAX-USD",
    "MATIC": "MATIC-USD",
    "TRX": "TRX-USD",
    "STETH": "STETH-USD",
    "WBTC": "WBTC-USD",
    "LEO": "LEO-USD",
    "ETC": "ETC-USD",
    "LTC": "LTC-USD",
}


def getCryptoByRangeData(ticker, startDate, endDate, interval):
    crypto_df = yf.download(ticker, startDate, endDate, interval=interval)
    df = crypto_df.reset_index(level=0)
    return df


start = datetime(2015, 1, 1)
end = datetime(2023,9,25)
interval = "1d"

data = getCryptoByRangeData("BTC-USD",start, end, interval)

print(data)