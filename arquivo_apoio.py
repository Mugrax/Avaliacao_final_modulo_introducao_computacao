import csv

# arquivos='alunos.csv'


def conversao_bool(monitoria):
    if monitoria == 'True':
        x = True
    else:
        x = False
    return x


def conversao_discionario(arquivos,delimitador):
    arquivo=open(arquivos,'r')
    iterador=csv.reader(arquivo,delimiter=delimitador)

    typ_list=[str,int,str,float,float,int,float,conversao_bool]
    lista = []
    lista += iterador
    lista_discionario = []

    for atributo_chave in lista[1:]:
        discionario = {}
        for indice,chave in enumerate(lista[0]):
            typ = typ_list[indice]
            discionario[chave] = typ(atributo_chave[indice])
        lista_discionario += [discionario]

    return lista_discionario


def contador_discionario(discionario,chave):

    lista_discionario = {}

    for i in discionario:
        chaves = i[chave]
        if chaves not in lista_discionario:
            lista_discionario[chaves] = 1
        else:
            lista_discionario[chaves] += 1

    return lista_discionario


    
# lista=conversao_discionario(arquivos,',')
# discionario=contador_discionario(lista,'escola')
# print(lista)