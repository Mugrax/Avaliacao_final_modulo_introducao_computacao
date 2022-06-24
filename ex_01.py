from arquivo_apoio import conversao_discionario as cvd
from arquivo_apoio import contador_discionario as ctd
arquivos='alunos.csv'

#Quantos alunos estudam em cada escola, e qual a escola com mais alunos

lista=cvd(arquivos,',')

escolas_alunos=ctd(lista,'escola')

escolas_alunos=escolas_alunos.items()

escola_mais_alunos=0
maior_escola=''

for i in escolas_alunos:
    
    print(f'Escola: {i[0]}\nAlunos: {i[1]}\n')

    if escola_mais_alunos < i[1]:
        escola_mais_alunos += i[1]
        maior_escola = i[0]


print(f'Escola com mais alunos: {maior_escola}\n')