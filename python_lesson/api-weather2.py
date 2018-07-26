import requests
import json

#json.decoder.JSONDecodeError: Extra dataによるエラーが表示されなくなった。
#apiのひな型のスペルが間違っていたため読み込むjsonファイルがないとエラー


# APIキーの指定
apikey = ""

#都市名
cities = ["Tokyo,JP", "London,UK", "New York,US"]
# APIのひな型
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

k2c = lambda k: k - 273.15

for name in cities:

    url = api.format(city=name, key=apikey)

    r = requests.get(url)

    data = json.loads(r.text)  
    
    # 結果を表示
    print("都市:", data["name"])
    print("天気:", data["weather"][0]["description"])
    print("最低気温:", k2c(data["main"]["temp_min"]))
    print("最高気温:", k2c(data["main"]["temp_max"]))
    print("湿度:", data["main"]["humidity"])
    print("気圧:", data["main"]["pressure"])
    print("風向き:", data["wind"]["deg"])
    print("風速:", data["wind"]["speed"])
    print("")
