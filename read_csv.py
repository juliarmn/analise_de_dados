import pandas as pd
#Lembre que deve estar na mesma pasta -> senão passar caminho
dataframe = pd.read_csv('jua.csv', sep=';')
print(dataframe)

#Código simples para pegar informações de arquivos csv
#Se for passar caminho, colocar r na frente (raw_string)

#Colunas como chave de dicionário
print('\n\n')
print(dataframe['cor'])

#Até uma linha apenas:
#Linhas são como listas
print('\n\n')
print(dataframe[:3])

#Passar mais de uma coluna:
print('\n\n')
print(dataframe[['cor', 'quantidade']])

#Pegar só um valor:
print('\n\n')
print(dataframe['cor'][3])