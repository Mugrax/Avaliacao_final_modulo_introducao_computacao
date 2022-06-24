from arquivo_apoio import conversao_discionario as cvd

arquivos='alunos.csv'

# Quantos alunos do 3 ano reprovaram? e desses quantos procuraram monitoria?

discionario = cvd(arquivos,',')


alunos_reprovados = 0
alundos_monitoria_true = 0


for i in discionario:
    if i['ano'] == 3:
        media = (i['nota_semestre_1'] + i['nota_semestre_2'])/2
        if media < 7:
            if i['nota_exame'] <= 5:
                if i['monitoria'] == True:
                    alundos_monitoria_true += 1
                    alunos_reprovados += 1
                else:
                    alunos_reprovados += 1

print(f'\nalunos do terceiro ano reprovados: {alunos_reprovados}\n\nAlunos reprovados que buscaram monitoria: {alundos_monitoria_true}\n')