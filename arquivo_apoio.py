import csv
from re import I

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

def reprovados(discionario):
    lista=[]
    for i in discionario:
        
        ambas=False
        faltas=False
        media_exame=False
        ano=i['ano']

        media = (i['nota_semestre_1'] + i['nota_semestre_2'])/2

        if media < 7 and i['nota_exame'] <= 5 and i['faltas'] > 15:
            ambas=True
        elif i['faltas'] > 15:
            faltas=True
        elif media < 7 and i['nota_exame'] <= 5:
            media_exame=True
        if not(ambas == False and faltas == False and media_exame == False):
            lista+=[[ano,ambas,faltas,media_exame]]

    return lista

    
# lista=conversao_discionario(arquivos,',')
# discionario=contador_discionario(lista,'escola')
# print(lista)