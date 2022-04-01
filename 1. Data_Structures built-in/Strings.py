text = "X-DSPAM-Confidence:    0.8475"
colon = text.find(':')
liczba = text[colon + 1:]
liczba1 = liczba.strip()
liczba2 = float(liczba1)

print(colon)
print(liczba)
print(liczba1)
print(liczba2)
