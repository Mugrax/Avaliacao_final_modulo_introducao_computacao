from arquivo_apoio import conversao_discionario as cvd
from arquivo_apoio import reprovados as rp
from matplotlib import pyplot


arquivos = 'alunos.csv'

'''
    As reprovações são maiores entre os alunos do 1º, 2º ou 3º ano?. Crie um
    gráfico para mostrar isso.

'''

discionario = cvd(arquivos,',')
reprovados = rp(discionario)

primeiro_ano=0
segundo_ano=0
terceiro_ano=0
base=['1º Ano','2º Ano','3º Ano']

for i in reprovados:
    if i[0] == 1:
        primeiro_ano+=1
    elif i[0] == 2:
        segundo_ano+=1
    else:
        terceiro_ano+=1

lista=[primeiro_ano,segundo_ano,terceiro_ano]

fig, ax = pyplot.subplots()
ax.bar(base,lista)
pyplot.show()