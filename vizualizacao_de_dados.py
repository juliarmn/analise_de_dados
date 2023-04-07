#Exibição de gráficos
import pandas as pd
vendas_dataFrame = pd.read_csv(r'dados.csv', sep=';')
clientes_dataFrame = pd.read_csv(r'clientes.csv', sep=';')
clientes_dataFrame = clientes_dataFrame[['ID Cliente']]
print(vendas_dataFrame.head())
print(clientes_dataFrame.head())
vendas_dataFrame['Custo Unitario'] = vendas_dataFrame['Custo Unitario'].str.replace(',', '.').astype(float)
vendas_dataFrame['Preco Unitario'] = vendas_dataFrame['Preco Unitario'].str.replace(',', '.').astype(float)
print(vendas_dataFrame.head())
print(clientes_dataFrame.head())
#vendas_dataFrame = vendas_dataFrame.merge(clientes_dataFrame, on='ID Cliente')

#Seleciona somente a coluna 'ID Cliente' do DataFrame clientes_dataFrame
clientes_id = clientes_dataFrame[['ID Cliente']]
#Realiza a mesclagem dos DataFrames vendas_dataFrame e clientes_id pelo ID do cliente
vendas_dataFrame = vendas_dataFrame.merge(clientes_dataFrame, on='ID Cliente')