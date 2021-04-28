import re
a = ('E:/Edukacja/Programowanie/Python/Python_Projekty/py4e/11/aktualne.txt')
fhandle = open(a)
lista = list()
# for line in fhandle:
#     line = line.rstrip()
#     pattern = re.findall(r'[0-9]+',line)
#     lista = lista + pattern

print(sum( map(int,re.findall('[0-9]+',fhandle.read()) ))) 


# suma_ = 0
# for i in lista:
#     suma_ = suma_ + int(i)
# print(lista)
# print(suma_)

#read geting content in string format