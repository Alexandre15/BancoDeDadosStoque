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
    cont = 0
    cursor.execute("SHOW DATABASES")
    bancos = cursor.fetchall()
    print("Bancos de dados disponíveis:\n")
    for c in bancos:
        print(f"{c[0]}", end=' | ')


def inquiryT():
    cursor.execute("SHOW TABLES")
    tabelas = cursor.fetchall()
    print("Tabelas disponíveis:\n")
    for c in tabelas:
        print(f"{c[0]}")



inquiryB()
inquiryT()