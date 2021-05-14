# fname = input("Enter file name: ")
adres = "mbox-short.txt"


fname = input(adres)
counter = 0
fh = open(adres)

for line in fh :
    line = line.rstrip()
    if not line.startswith('From '): 
        continue        
    words = line.split()
    print (words[1])
    counter +=1

print ("There were", counter, "lines in the file with From as the first word")

 	