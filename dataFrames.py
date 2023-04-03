#Colunas como chaves de dicionários
#Linhas como listas
import pandas as pd
from IPython.display import display
vendas_dataFrame = pd.read_csv('dados.csv', sep=';')
print(vendas_dataFrame['Categoria'])
print(vendas_dataFrame[:3])
#Se pegar a linha com índice 0 dá erro, tem que ser até alguma linha

#Integração de bases de dados diferentes:
clientes_dataFrame = pd.read_csv(r'clientes.csv', sep=';')
promocoes_dataFrame = pd.read_csv(r'promocoes.csv', sep=';')
display(vendas_dataFrame)
display(clientes_dataFrame)
display(promocoes_dataFrame)
#Erro de encoding: encoding='ISO-8859-1', encoding='utf-8'...->coloca após o sep

#Retirar colunas:
clientes_dataFrame = clientes_dataFrame.drop(['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9'], axis = 1)
display(clientes_dataFrame)
clientes_dataFrame = clientes_dataFrame[['ID Cliente']]
print(clientes_dataFrame)
promocoes_dataframe = promocoes_dataFrame[['ID Promocao', 'Nome Promocao']]
print(promocoes_dataframe)
vendas_dataFrame = vendas_dataFrame[['Categoria', 'ID Produto']]
display(vendas_dataFrame)

#on=['nome coluna']:
#clientes_dataFrame = clientes_dataFrame.merge(promocoes_dataFrame, on='ID Promocao')
# clientes_dataFrame = clientes_dataFrame.merge(vendas_dataFrame, on='Categoria')
# display(vendas_dataFrame)
# vendas_dataFrame = vendas_dataFrame.rename(columns={'Categoria': 'categoria'})
display(vendas_dataFrame)