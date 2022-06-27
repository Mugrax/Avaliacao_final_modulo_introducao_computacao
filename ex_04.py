from arquivo_apoio import conversao_discionario as cvd

arquivos = 'alunos.csv'

'''
    De todos os alunos que reprovaram quantos foram por falta e quantos foram
    por nota, e quantos foram por ambas as causas?
'''

discionario=cvd(arquivos,',')

alunos_ambas = 0
alunos_falta = 0
alunos_nota = 0

for i in discionario:
    media = (i['nota_semestre_1'] + i['nota_semestre_2']) / 2
    if media < 7 and i['nota_exame'] <= 5 and i['faltas'] > 15:
       alunos_ambas += 1
       alunos_falta += 1
       alunos_nota += 1
    elif i['faltas'] > 15:
        alunos_falta += 1
    elif media < 7 and i['nota_exame'] <= 5:
        alunos_nota += 1

alunos_so_nota = alunos_nota - alunos_ambas
alunos_so_falta = alunos_falta - alunos_ambas

print(f'\nAlunos que reprovaram por faltas e notas: {alunos_ambas}\n')
print(f'Alunos que reprovaram por faltas: {alunos_falta}\nAlunos que reprovaram só por faltas: {alunos_so_falta}\n')
print(f'Alunos que reprovaram por nota: {alunos_nota}\nAlunos que reprovaram só por nota: {alunos_so_nota}\n')
