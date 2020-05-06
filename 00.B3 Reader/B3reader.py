fileHandler = open("./COTAHIST.TXT","r",encoding = "utf-8")

lines = fileHandler.readlines()
lines.pop()

fileHandler.close()


print((lines[1][2:10]))

def leitor_01 (linha):
    lista = []
    lista.append(linha[:2]) #0
    lista.append(linha[2:10]) #1
    lista.append(linha[10:12]) #2
    lista.append(linha[12:24]) #3
    lista.append(linha[24:27]) #4
    lista.append(linha[27:39]) #5
    lista.append(linha[39:49]) #6
    lista.append(linha[49:52]) #7
    lista.append(linha[52:56]) #8
    lista.append(linha[56:69]) #9 float
    lista.append(linha[69:82]) #10 float
    lista.append(linha[82:95]) #11 float
    lista.append(linha[95:108]) #12 float
    lista.append(linha[108:121]) #13 float
    lista.append(linha[121:134]) #14 float
    lista.append(linha[134:147]) #15 float
    lista.append(linha[147:152]) #16 int
    lista.append(linha[152:170]) #17 int
    lista.append(linha[170:188]) #18 float
    lista.append(linha[188:201]) #19 float
    lista.append(linha[201:202]) #20 int
    lista.append(linha[202:210]) #21 int
    lista.append(linha[210:217]) #22 int
    lista.append(linha[217:230]) #23
    lista.append(linha[230:242]) #24
    lista.append(linha[242:245]) #25

    lista = [campo.strip() for campo in lista]

    lista[9] = float(lista[9])/100
    lista[10] = float(lista[10])/100
    lista[11] = float(lista[11])/100
    lista[12] = float(lista[12])/100
    lista[13] = float(lista[13])/100
    lista[14] = float(lista[14])/100
    lista[15] = float(lista[15])/100
    lista[16] = int(lista[16])
    lista[17] = int(lista[17])
    lista[18] = float(lista[18])/100
    lista[19] = float(lista[19])/100

    return lista    


    

import csv
header= ["Tipo_de_Registro", "Data_do_Pregao","Codigo_BDI", "Codigo_de_Negociacao","Tipo_de_Mercado","Empresa","Especificacao","Prazo_a_Termo","Moeda","Preco_Abertura","Preco_Maximo","Preco_Minimo","Preco_Medio","Preco_Fechamento","Preco_Maior_Oferta_Compra","Preco_Maior_Oferta_Venda","Numero_de_Negocios","Quantidade_Negociada","Volume_Negociado","Preco_de_Exercicio","Indicador_de_Correcao","Data_de_Vencimento","Fator_de_Cotacao","PTOEXE","ISIN","Num_de_Distribuicao"]
with open("./ArquivoFinal.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    for i in lines[1:]:
        writer.writerow(leitor_01(i))
    
    

