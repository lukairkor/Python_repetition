fname = input("Enter file name: ")

fh = open('E:/Edukacja/Programowanie/Python/Python_Projekty/py4e/8.4/romeo.txt','r')
odczyt = fh.read()
lst = list() #tworzenie listy

for line in odczyt.split():
    a = line
    if a in lst:
        continue
    lst.append(a)
lst.sort()
print(lst)

  


    

