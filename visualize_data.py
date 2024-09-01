import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

# Conectar ao banco de dados SQL Server
conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=localhost\SQLEXPRESS;DATABASE=AdventureWorks2022;Trusted_Connection=yes;')

# Executar uma consulta SQL
df = pd.read_sql_query('SELECT TOP 10 * FROM [Sales].[Store]', conn)

# Exibir os primeiros registros (opcional)
print(df.head())

# Criar um gráfico simples
df['Count'] = 1  # Adiciona uma coluna de contagem
df.groupby('Name')['Count'].count().plot(kind='bar')  # Agrupa por Name e conta
plt.title('Sales Stores')
plt.xlabel('Store Name')
plt.ylabel('Count')
plt.show()
