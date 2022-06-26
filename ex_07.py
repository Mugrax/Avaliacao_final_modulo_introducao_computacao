from matplotlib import pyplot
from arquivo_apoio import conversao_discionario as cvd

arquivos = 'alunos.csv'

'''
    Qual dos anos (1º, 2º ou 3º) mais procura a monitoria?. Crie um gráfico para
    mostrar esses dados.

'''

discionario=cvd(arquivos,',')

alunos_1=0
alunos_2=0
alunos_3=0

for i in discionario:
    if i['ano'] == 1:
        if i['monitoria'] == True:
            alunos_1+=1
    elif i['ano'] == 2:
        if i['monitoria'] == True:
            alunos_2+=1
    else:
        if i['monitoria'] == True:
            alunos_3+=1

base=['Primeiro Ano','Segundo Ano','Terceiro Ano']
lista=[alunos_1,alunos_2,alunos_3]

fig, ax = pyplot.subplots()
ax.bar(base,lista)
pyplot.show()
