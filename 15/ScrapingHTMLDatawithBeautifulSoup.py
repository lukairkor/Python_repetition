from urllib.request import urlopen
from bs4 import BeautifulSoup # importujemy class z pliku __init__.py w folder bs4
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

suma = 0
lista = list()

url = 'http://py4e-data.dr-chuck.net/comments_169389.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())

tags = soup('span')
for tag in tags:
    suma = suma+int(tag.contents[0])
print(suma)

    
    
    
    
    
    
    


    