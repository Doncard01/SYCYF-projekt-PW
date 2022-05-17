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
    tabA.pop(len(tabA) - 1)
    tabB.pop(len(tabB) - 1)
    sent.pop(len(sent) - 1)

pointA = np.array(tabA, dtype=float)
pointB = np.array(tabB, dtype=float)
sent1 = np.array(sent, dtype=float)
wynikiA = []

suma=0.0
for i in range(len(pointA)-20):
    wynikiA.append(suma)
    suma = 0.0
    for j in range(len(sent1)):
        if pointA[i + j] > sent1[j]:
            suma = suma + pointA[i + j] - sent1[j]

        else:
            suma = suma + sent1[j] - pointA[i + j]


wynikAgit = np.array(wynikiA, dtype=float)
wynikAgit = np.delete(wynikAgit,0)
maxA = np.argmin(wynikAgit)

print(maxA)
