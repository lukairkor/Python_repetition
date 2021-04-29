# def funkcja (x,y,*z):
#     a = x + y 
#     return print(a,'\n',sum(z))

# funkcja(2,2,2,2,2,2,2)

import re

tekst = 'We just received $10.00 for cookies.'
sciezka = r'[0-9a-zA-Z.].+'
dopasowanie = re.findall(sciezka, tekst)

print(dopasowanie)

