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
korA = sig.correlate(sent, pointA)
korB = sig.correlate(sent, pointB)

maxA = np.argmax(korA)
maxB = np.argmax(korB)

print(f"Korelacja dla A: {maxA}, \nKorelacja dla B: {maxB}")

roznica = maxA - maxB
print(f"Różnica dla @korA i @korB: {roznica}")


