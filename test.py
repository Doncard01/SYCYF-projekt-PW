import numpy as np
import matplotlib.pyplot as plt

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


def metodaRoznicy(wzor, pacjent):
    wynikiA = []
    for i in range(len(pacjent) - 20):

        suma = 0.0
        for j in range(len(wzor)):
            suma = suma + abs(pacjent[i + j] - wzor[j])
        wynikiA.append(suma / 20)
    return wynikiA

if __name__ == '__main__':
    temp1 = metodaRoznicy(sent1, pointA)
    wynikAgit = np.array(temp1, dtype=float)
    minA = np.argmin(wynikAgit)
    print(minA)
    temp2 = metodaRoznicy(sent1, pointB)
    wynikBgit = np.array(temp2, dtype=float)
    minB = np.argmin(wynikBgit)
    print(minB)


    x_coordinate = [1 * i for i in range(len(wynikAgit))]
    plt.axis([1630, 1670, 0.2, 0.9])
    # pointAD=pointB
    # for i in range(20):
    #     pointAD = np.delete(pointAD,4980)

    #plt.plot(x_coordinate, wynikAgit)

    plt.plot(x_coordinate, wynikBgit)
    # plt.plot(x_coordinate, pointAD)
    plt.show()


