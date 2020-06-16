num = 219456894
possibilidades = []


for i in range(2,num):

    if num % i == 0:
        possibilidades.append(i)

import csv

with open("./lista_primos.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(possibilidades)