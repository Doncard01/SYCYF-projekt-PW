import numpy as np
import scipy.signal as sig

tabA = []
tabB = []
sent = []

with open("pointA.txt", "r") as fp:
    lines = fp.readlines()
    for line in lines:
        a = line.strip()
        tabA.append(a)

with open("pointB.txt", "r") as fp:
    lines = fp.readlines()
    for line in lines:
        b = line.strip()
        tabB.append(b)

with open("sent8.txt", "r") as fp:
    lines = fp.readlines()
    for line in lines:
        s = line.strip()
        sent.append(s)

for i in range(5):
    tabA.pop(0)
    tabB.pop(0)
    sent.pop(0)

for i in range(2):
    tabA.pop(len(tabA)-1)
    tabB.pop(len(tabB)-1)
    sent.pop(len(sent)-1)

pointA = np.array(tabA, dtype=float)
pointB = np.array(tabB, dtype=float)
sent = np.array(sent, dtype=float)

# print(pointA)
# print(pointB)
# print(sent)


#korelacja
korA = sig.correlate(pointA, sent)
korB = sig.correlate(pointB, sent)

maxA = np.argmax(korA)
maxB = np.argmax(korB)

print(f"Korelacja dla A: {maxA} próbka \nKorelacja dla B: {maxB} próbka\n")


c = 300000
#oba promienie dzielone na 2, ponieważ sygnał musiał w tym czasie pokonać drogę do drona i z powrotem
promienA = (maxA*10**(-6)*c)/2
promienB = (maxB*10**(-6)*c)/2
print(f"Promień dla A: {promienA}km")
print(f"Promień dla B: {promienB}km")
