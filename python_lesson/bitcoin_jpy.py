from bs4 import BeautifulSoup
import urllib.request as req

# HTMLを取得
url = "https://cc.minkabu.jp/pair/BTC_JPY"
res = req.urlopen(url)

# HTMLを解析
soup = BeautifulSoup(res, "html.parser")

# BIT/JPYのデータを抽出 --- (※1)
price = soup.select_one("#btc_jpy_top_bid").string
#print("bit/jpy=" , price)
print(price)
