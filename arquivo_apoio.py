import csv

arquivos='alunos.csv'

def conversao_discionario(arquivos,delimitador):
    arquivo=open(arquivos,'r')
    iterador=csv.reader(arquivo,delimiter=delimitador)

    lista=[]
    lista+=iterador
    lista_discionario=[]

    for atributo_chave in lista[1:]:
        contador_indice=0
        discionario={}
        for chave in lista[0]:
            discionario[chave]=atributo_chave[contador_indice]
            contador_indice+=1
        lista_discionario+=[discionario]
    return lista_discionario
    
# lista=conversao_discionario(arquivos,',')
# print(lista)