import urllib.request
from bs4 import BeautifulSoup

# 기온데이터를 저장할 파일을 쓰기모드로 연다
f = open('wunder-data-seoul.txt', 'w')

# 1월에서 12월까지 각 날짜의 페이지를 순회하면서 기온정보를 뽑아낸다
for m in range(1, 13):
    for d in range(1, 32):
        if (m == 2 and d > 28):  # 2월이 28일을 넘으면 중단하고 다음 달로 넘어간다
            break
        elif (m in [4, 6, 9, 11] and d > 30):  # 4, 6, 9, 11월이 30일을 넘으면 중단하고 다음 달로 넘어간다
            break

        if (len(str(m)) == 1) and (len(str(d)) == 1):
            timestamp = '20130' + str(m) + '0' + str(d)
        elif (len(str(m)) == 1) and (len(str(d)) == 2):
            timestamp = '20130' + str(m) + str(d)
        elif (len(str(m)) == 2) and (len(str(d)) == 1):
            timestamp = '2013' + str(m) + '0' + str(d)
        else:
            timestamp = '2013' + str(m) + str(d)

        # 뽑아내려는 기온데이터가 들어있는 페이지를 urllib 라이브러리로 불러온다
        url = "http://english.wunderground.com/history/airport/RKSS/2013/" \
              + str(m) + "/" + str(d) + \
              "/DailyHistory.html?req_city=NA&req_state=NA&req_statename=NA"
        print(url)
        page = urllib.request.urlopen(url)

        # Beautiful Soup 라이브러리로 기온데이터를 추출한다.
        # 기온데이터는 nobr 클래스에 span태그로 둘러싸여 있다.
        soup = BeautifulSoup(page, "lxml")
        #soup = BeautifulSoup(page, "html.parser")
        print(soup.prettify())
        dayMeanTemp = soup.find_all('span', attrs={"class": "wx-value"})[0].string
        dayMaxTemp = soup.find_all('span', attrs={"class": "wx-value"})[1].string
        dayMinTemp = soup.find_all('span', attrs={"class": "wx-value"})[2].string

        print('date: {0},{1},{2},{3}'.format(timestamp, dayMeanTemp, dayMaxTemp, dayMinTemp))

        if len(str(m)) < 2:
            mStamp = '0' + str(m)
        else:
            mStamp = str(m)

        if len(str(d)) < 2:
            dStamp = '0' + str(d)
        else:
            dStamp = str(d)

        timestamp = '2013' + mStamp + dStamp

    # 읽어온 기온데이터를 파일에 쓴다
    f.write(timestamp + ',' + dayMeanTemp + ',' + dayMaxTemp + ',' + dayMinTemp + '\n')

# 모든 데이터를 읽었으면, 기온데이터를 저장한 파일을 닫는다
f.close()