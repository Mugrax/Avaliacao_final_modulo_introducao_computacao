from arquivo_apoio import conversao_discionario as cvd

arquivos = 'alunos.csv'
'''
    Qual a média de todas as notas (do 1º e 2º semestre) 
    dos alunos do 2º ano?
'''

discionario=cvd(arquivos,',')

media_1=0
media_2=0
media_da_media=0
media_da_media_2=0
dividendo=0

for i in discionario:
    if i['ano'] == 2:
        dividendo+=1
        media_1+=i['nota_semestre_1']
        media_2+=i['nota_semestre_2']
        media_da_media+=(i['nota_semestre_1'] + i['nota_semestre_2'])/2

media_1/=dividendo
media_2/=dividendo
media_da_media/=dividendo

print(f'\nA média do 1º semestre é: {round(media_1,2)}\n')
print(f'A média do 2º semestre é: {round(media_2,2)}\n')
print(f'A média de todas as notas é: {round(media_da_media,2)}\n')
