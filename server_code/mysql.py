import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
import mysql.connector
from anvil.server import callable

def get_db_connection():
    connection = mysql.connector.connect(
        host='192.168.1.12',       # z.B. 'localhost' oder die IP-Adresse Ihres Datenbankservers
        user='root',   # Ihr Datenbankbenutzername
        password='Sensid.DB',# Ihr Datenbankpasswort
        database='tooltronic'    # Der Name Ihrer Datenbank
    )
    return connection

@callable
def fetch_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM measurement")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result