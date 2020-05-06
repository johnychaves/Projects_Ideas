import xml.etree.ElementTree as ET

arquivo = "XML_Carteiras.xml"
tree = ET.parse(arquivo)

root = tree.getroot()
# print(root)

# filtro = "*"
# for child in root.iter(filtro):
#     print(child.tag, child.text)
lista_codcart = []
lista_patliq = []
lista_valorreceber = []
lista_valorpagar = []
lista_valorativos = []
lista_consolidada = []
lista_caixa = []

for child in root.findall("carteira"):
    for title in child.findall("header"):

        for codigo in title.findall("codcart"):
            lista_codcart.append(codigo.text)    

        for patrimonio in title.findall("patliq"):
            lista_patliq.append(patrimonio.text)
        
        for valor_a_receber in title.findall("valorreceber"):
            lista_valorreceber.append(valor_a_receber.text)
        
        for valor_a_pagar in title.findall("valorpagar"):
            lista_valorpagar.append("-" + valor_a_pagar.text)
        
        for valor_ativos in title.findall("valorativos"):
            lista_valorativos.append(valor_ativos.text)

    for title in child.findall("caixa"):
        for caixa in title.findall("saldo"):
            lista_caixa.append(caixa.text)


# print(len(lista_codcart))
# print(len(lista_patliq))
# print(len(lista_valorreceber))
# print(lista_valorpagar)
# print(len(lista_valorativos))


# for i, _ in enumerate(lista_patliq):
    
#     lista_caixa.append(round(float(lista_patliq[i]) - float(lista_valorpagar[i]) - float(lista_valorreceber[i]) - float(lista_valorativos[i]),2))

for i , _ in enumerate(lista_codcart):
    
    lista_consolidada.append([lista_codcart[i],lista_patliq[i],lista_caixa[i],lista_valorreceber[i],lista_valorpagar[i],lista_valorativos[i]])




import csv
header= ['CodigoCliente', 'PatrimonioLiq','Caixa' ,'Valores_a_receber', 'Valores_a_pagar', 'Valor_ativos']
with open("./CarteirasConsolidadas.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    for elemento in lista_consolidada:
        writer.writerow(elemento)


