from bs4 import BeautifulSoup 
from urllib.request import urlopen 

html = urlopen("http://naver.com") 
soup = BeautifulSoup(html.read(), "lxml") 

# for row in soup.find_all("ol"):
#     print(row)
#     for i in range(11):
#         try:
#             li = row.find_all("li", attrs={"value":str(i)})
#             print(li)
#             st1 = str(li).split(">")[1]
#             print(st1)
#             st2 = st1.split("title=")[1] #인터파크 등의 인기검색어
#             print("%d => %s" % (i, st2))
#         except:
#             print("--- 네이버 인기 검색어 ---")

# for row in soup.find_all("ol"):
#     for i, li in enumerate(row.find_all("li")):
#         print("%d => %s" % (i, li.find("a").get("title")))




for i , row in enumerate(soup.select("ol > li > a")):
        print("%d => %s" % (i, row.get("title")))