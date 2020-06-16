#Combina 1 (29,79)
#Combina 2 (127,877)
#Combina 3 (4,257)
#Combina 4 (11,5)
#Combina 5 (22)
#Combina 6 (125)
#Combina 7 (8,2)
#Combina 8 (2,17)

combina7 = []
combina8 = []


teste = 123456789


while teste <= 987654321:

    if teste % 8 == 0:
        
        teste2 = int(str(teste)[::-1])
        if teste2 % 2 == 0:

            if len(set(str(teste))) == 9 and '0' not in str(teste):
                combina7.append(teste)

    if teste % 2 == 0:
        
        teste2 = int(str(teste)[::-1])
        if teste2 % 17 == 0:

            if len(set(str(teste))) == 9 and '0' not in str(teste):
                combina8.append(teste)        

        
    # if teste % 22 == 0:
    #     if len(set(str(teste))) == 9 and '0' not in str(teste):
    #         combina5.append(teste)

    # if teste % 125 == 0:
    #     if len(set(str(teste))) == 9 and '0' not in str(teste):
    #         combina6.append(teste)

    # if teste % 4 == 0:
    #     teste2 = int(str(teste)[::-1])
    #     if teste2 % 257 == 0:
    #         if len(set(str(teste))) == 9 and '0' not in str(teste):
    #             combina3.append(teste)


    teste+=1



import csv

with open("./Combinacoes7.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(combina7)
    
with open("./Combinacoes8.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=";")
    writer.writerow(combina8)

# with open("./Combinacoes6.csv", "w", newline="") as csvfile:
#     writer = csv.writer(csvfile, delimiter=";")
#     writer.writerow(combina6)
