text = "X-DSPAM-Confidence:    0.8475"
colon = text.find(':')
liczba = text[colon+1:]
liczba = liczba.strip()
liczba = float(liczba)
print(liczba)