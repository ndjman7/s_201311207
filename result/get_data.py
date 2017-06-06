import csv
import requests
from bs4 import BeautifulSoup


day2 = [
    '20150101','20150102','20150103','20150104','20150105','20150106',
    '20150107','20150108','20150109','20150110','20150111','20150112',
    '20150113','20150114','20150115','20150116','20150117','20150118',
    '20150119','20150120','20150121','20150122','20150123','20150124',
    '20150125','20150126','20150127','20150128','20150129','20150130',
    '20150131'
]

def music_genre(date):
    # 음악 장르 빈도수
    d = dict()
    count = 0
    r = requests.get('http://music.bugs.co.kr/chart/track/realtime/total?chartdate={}&charthour={}'.format(date, '12'))
    music_list = BeautifulSoup(r.text, 'html.parser')
    m_list = music_list.find('tbody').find_all('tr')
    for music in m_list:
        if music.th.p.find('a'):
            r2 = requests.get(music.find_all('td')[2].a.get('href'))
            bs2 = BeautifulSoup(r2.text,'html.parser')
            for genre in bs2.find('tbody').find_all('tr')[4].td.find_all('a'):
                if d.get(genre.text) == None:
                    d[genre.text] = 0
                else:
                    d[genre.text] += 1
                count += 1
    
    # 날씨 온도
    l = []
    r = requests.get('http://www.kma.go.kr/weather/climate/past_cal.jsp?stn=108&yy={}&mm={}'.format(date[:4],date[4:6]))
    bs = BeautifulSoup(r.text, 'html.parser')
    data = bs.tbody.find_all('tr')
    for weather_list in data[1::2]:
        for weather in weather_list.find_all('td'):
            if len(weather.text) > 2:
                l.append(weather.text.encode('utf-8').split('℃최고')[0].split('기온:')[1])
    
    
    return [date, round(d[u'발라드']/float(count),2), l[int(date[6:])-1]]

with open('../musicdata/data.csv', 'w') as csvfile: 
        writer = csv.writer(csvfile, delimiter=',')        
        for date in day2:
            val = music_genre(date)
            writer.writerow(val)