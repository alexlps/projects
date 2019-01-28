import csv

open_file =open('c:\\teste\\wordcount.txt','r')

# deixando tudo minúsculo

file = open_file.read().lower()

#removendo caracteres indesejados se houver

file = file.replace("\n","")
file = file.replace(".","")
file = file.replace("!","")
file = file.replace("?","")
file = file.replace(",","")
file = file.replace(";","")
file = file.replace("á","a")
file = file.replace("à","a")
file = file.replace("ã","a")
file = file.replace("é","e")
file = file.replace("ê","e")
file = file.replace("í","i")
file = file.replace("ó","o")
file = file.replace("ô","o")
file = file.replace("ú","u")
file = file.replace("ç","c")


# Criando lista Inicial
 
lista_inicial = (file.split(" "))


# Obtendo quantidade de palavras que possuem menos de 10 letras
word_count = []
for x in sorted(set(lista_inicial)):
    if len(x) <= 10:
        word_count.append((x,lista_inicial.count(x))) 

# Obtendo quantidade de palavras que possuem mais de 10 letras

maiores_10 = []

for y in sorted(set(lista_inicial)):
    if len(y) > 10:
        maiores_10.append((lista_inicial.count(y)))
        total = sum(maiores_10)

# Insere quantidade das palavras que contem mais de dez letras na lista        
word_count.append(("MAIORES QUE DEZ",total))


# Export to CSV

with open('c:\\teste\word_count_alex.csv', "w") as output:
    writer = csv.writer(output, lineterminator=','+'\n')
    for val in word_count:
        writer.writerow([val])    

output.close()
open_file.close()
                

