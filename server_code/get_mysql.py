import anvil.server
import mysql.connector
from anvil.server import callable

def get_db_connection():
  try:
    connection = mysql.connector.connect(
        host='192.168.1.12',       # z.B. 'localhost' oder die IP-Adresse Ihres Datenbankservers
        user='root',   # Ihr Datenbankbenutzername
        password='Sensid.DB',# Ihr Datenbankpasswort
        database='tooltronic'    # Der Name Ihrer Datenbank
    )
    
    return connection
  except mysql.connector.Error as err:
        print(f"Datenbankverbindungsfehler: {err}")
        raise