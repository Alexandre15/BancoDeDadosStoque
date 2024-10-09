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
    print("Conectado com a bodega")
else:
    print("Fudeu")


def inquiry():
    cursor.execute("SHOW DATABASES")
    bancos = cursor.fetchall()
    print("Bancos de dados disponíveis:")
    print(bancos[0])

inquiry()