import pandas as pd
from sqlalchemy import create_engine

def get_connection():
    # Lista de strings de conexão para testar
    connection_strings = [
        # "mssql+pyodbc://username:password@localhost/database?driver=ODBC+Driver+17+for+SQL+Server",
        # "mssql+pyodbc://username:password@localhost\\SQLEXPRESS/database?driver=ODBC+Driver+17+for+SQL+Server",
        # "mssql+pyodbc://username:password@127.0.0.1/database?driver=ODBC+Driver+17+for+SQL+Server",
        # "mssql+pyodbc://username:password@127.0.0.1\\SQLEXPRESS/database?driver=ODBC+Driver+17+for+SQL+Server",
        "mssql+pyodbc://@localhost\\SQLEXPRESS/AdventureWorks2022?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"  # Nova string de conexão adicionada
        # Adicione mais strings de conexão conforme necessário
    ]

    for conn_str in connection_strings:
        try:
            print(f"Trying connection: {conn_str}")
            engine = create_engine(conn_str)
            connection = engine.connect()
            print("Connection successful!")
            return connection  # Retorna a conexão bem-sucedida
        except Exception as e:
            print(f"Failed to connect using {conn_str}")
            print(f"Error: {e}")
    
    raise Exception("All connection attempts failed.")

def get_tables():
    conn = get_connection()
    query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'"
    tables = pd.read_sql_query(query, conn)
    conn.close()
    return tables['TABLE_NAME'].tolist()

def get_data(schema_name, table_name):  # Alterado para aceitar dois argumentos
    conn = get_connection()
    query = f'SELECT TOP 10 * FROM {schema_name}.{table_name}'  # Agora usando schema_name e table_name
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data

def get_schemas_and_tables():
    conn = get_connection()
    query = "SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'"
    schemas_and_tables = pd.read_sql_query(query, conn)
    conn.close()
    return schemas_and_tables
