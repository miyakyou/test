from bs4 import BeautifulSoup
import urllib.request as req


url = "https://www.aozora.gr.jp/index_pages/person148.html"
res  = req.urlopen(url)
soup = BeautifulSoup(res,"html.parser")

li_list = soup.select("ol > li")
for li in li_list:
    a = li.a
    #htmlの<a>でなくなるまで実行
    if a != None:
        name = a.string
      #  print(name)
    #「href=""」を表示    
        href = a.attrs["href"] 
        print(name,">",href)