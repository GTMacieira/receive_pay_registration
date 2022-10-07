# Bibliotecas utilizadas
import sqlite3
from sqlite3 import Error
from unittest import result

# Realizar conexão no banco de dados
def con_creator():
    # Desabilita qualquer conexão criada
    connection = None
    # Tenta conectar com banco de dados receive_pay_registration
    try:
        connection = sqlite3.connect("receive_pay_registration.db")
    # Caso não consiga conectar devolve o erro ao conectar
    except Error as err:
        pass
    return connection

def close_conection(conection):
    try:
        conection.close

    except:

        pass

# Executa querys
def execute_querys(query_type, query, connection):
    # Cria cursor interador para manipuçar o db
    cursor = connection.cursor()
    cursor.execute(query)
    # Realiza ação de acordo com o tipo de query
    try:
        if query_type == "INSERT" or query_type == "CREATE" or query_type == "DELETE":            
            try: 
                # Realiza alteração no banco
                connection.commit()
            except Error as err:
                print(f"Não foi possível realizar a ação, erro:\n {err}")
        elif query_type == "READ":
            try:
                # Lê banco de dados
                result = cursor.fetchall()
            except Error as err:
                print(f"Não foi possível realizar a ação, erro:\n {err}")
    except:
        pass 
    # Finaliza cursor
    cursor.close()

def select_all_empresas(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM empresas ORDER BY id")
        empresas = cursor.fetchall()
        return empresas
    except:
        pass
    
    
if __name__ == "__main__":
    connection = con_creator()
    execute_querys(
        "CREATE",
        """CREATE TABLE IF NOT EXISTS users(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
            user TEXT NOT NULL, password TEXT NOT NULL, 
            access NOT NULL, registro_db TIMEVALUE NOT NULL);""",
            connection)
    execute_querys(
        "CREATE",
        """CREATE TABLE IF NOT EXISTS empresas(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
            cnpj TEXT NOT NULL,  
            abertura DATE NOT NULL,  
            nome TEXT NOT NULL,  
            situacao TEXT NOT NULL,  
            logradouro TEXT NOT NULL,  
            numero TEXT NOT NULL,  
            complemento TEXT NOT NULL,  
            municipio TEXT NOT NULL, 
            uf TEXT NOT NULL,  
            porte TEXT NOT NULL, 
            tipo_cadastro TEXT NOT NULL,
            registro_db TIMEVALUE NOT NULL, 
            user TEXT NOT NULL);""",
            connection)
    execute_querys("CREATE",
        """CREATE TABLE IF NOT EXISTS recebimentos(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            valor_recebido NOT NULL,
            dta_recebimento DATE NOT NULL,
            data_registro TEMEVALUE NOT NULL,
            user TEXT NOT NULL);""",
            connection) 
    execute_querys("CREATE",
        """CREATE TABLE IF NOT EXISTS pagamentos(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            fornecedor TEXT NOT NULL, 
            valor_recebido NOT NULL, 
            dta_pagamento DATE NOT NULL, 
            data_registro DATETIME NOT NULL, 
            usuario TEXT NOT NULL)""",
            connection)