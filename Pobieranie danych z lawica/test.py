#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import ssl
import re
mport pandas as pd
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lista = [] #przechowuje wyniki do wyswietlenia 
#pobranie pliku html
url = 'https://www.airport-poznan.com.pl/pl/polaczenia-lotnicze/rozklad-lotow'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify())


# tags = soup.find_all("li" , attrs={"class" : "w70;w70" })
# tags1 = soup.find_all("ul" , attrs={"class" : "cityName"})
# # sciezka1 = r'<li>(.+[A-Ba-b].+)</li>'
# # sciezka2 = r'w70">(.+[A-Ba-b].+)</li>'

# tags_str = str(tags1)
# for i in tags:
#     print(i)

# #print(tags_str,'/n')

# # x = re.findall(sciezka1,tags_str)
# # y = re.findall(sciezka2,tags_str)
# # #
My_table = soup.find('div',{'class':'ArrivalsDepartures_Subpage tabs chtext'})

links = My_table.findAll('ul')

for link in links:
    print (link.text)
#     lista.append(link.get('text'))


# print(links)





# for t in lista:
#     print(t)

# # Retrieve all of the anchor tags
# tags = soup('article')
# for tag in tags:
#     print(tag.get('href', None))

