import mysql
import mysql.connector

conn = mysql.connector.Connect(
    user='root',
    password='Alex15',
    host='127.0.0.1',
    database='sakila'
)

cursor = conn.cursor()

if conn.is_connected():
    print("Conectado com a bodega...\n")
else:
    print("Fudeu kkk ....\n")


def inquiryB():
    """
    Mostra os Bancos disponíveis
    """
    cont = 0
    cursor.execute("SHOW DATABASES")
    bancos = cursor.fetchall()
    print("Bancos de dados disponíveis:\n")
    for c in bancos:
        print(f"{c[0]}", end=' | ')


def inquiryT():
    """
    Mostra as Tabelas disponíveis
    """
    cursor.execute("SHOW TABLES")
    tabelas = cursor.fetchall()
    print("Tabelas disponíveis:\n")
    for c in tabelas:
        print(f"{c[0]}")


def criar_banco(nome_banco: str):
    """
    Cria um banco de dados
    Parametros:
        nome_banco (str): Nome do banco
    """
    cursor.execute("CREATE DATABASE {}".format(nome_banco,))


def deletar_banco(nome_banco: str):
    """
    Deleta um banco de dados
    Parametros:
        nome_banco (str): Nome do banco
    """
    cursor.execute("DROP DATABASE {}".format(nome_banco,))


