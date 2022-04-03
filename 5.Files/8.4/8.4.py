fname = input("Enter file name: ")

fh = open('romeo.txt','r')
odczyt = fh.read()
lst = list() #tworzenie listy

for line in odczyt.split():
    a = line
    if a in lst:
        continue
    lst.append(a)
lst.sort()
print(lst)

  


    

