
fh = input("Enter file name: ")
# fh = open('E:/Edukacja/Programowanie/Python/Python_Projekty/py4e/7.2/mbox.txt','r')
fh = open('mbox-short.txt','r')
licznik = 0
ales = 0
avr = 0
for line in fh:
    #line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        line = line.strip()
        poz = line.find(':')
        line = line[poz+1:]
        line = float(line)
        ales = ales + line    
        licznik = licznik + 1
        licznik = float(licznik)
        avr = ales/licznik
        avr = float(avr)
        

avr = round(avr,12)
avr = str(avr)
avr = avr[:] 
print("Average spam confidence:", avr )




