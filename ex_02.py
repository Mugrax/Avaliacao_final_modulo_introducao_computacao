from arquivo_apoio import conversao_discionario as cvd

arquivos='alunos.csv'

#Quantos alunos do 1 ano foram aprovados sem exame?

discionario=cvd(arquivos,',')

quantidade_alunos_aprovados = 0

for i in discionario:
    if i['ano'] == 1:
        media = (i['nota_semestre_1'] + i['nota_semestre_2']) / 2
        if media >= 7 and i['faltas'] <= 15:
            quantidade_alunos_aprovados += 1

print(f'\n{quantidade_alunos_aprovados} Alunos do primeiro ano foram aprovados sem exame.\n')