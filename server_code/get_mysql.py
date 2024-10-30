import anvil.server
import mysql.connector
from anvil.server import callable

import anvil.server
#import anvil.logger
#import logging
#anvil.logger.set_default_logger()

def get_db_connection():
  try:
    connection = mysql.connector.connect(
        host='192.168.1.12',       # z.B. 'localhost' oder die IP-Adresse Ihres Datenbankservers
        user='root',   # Ihr Datenbankbenutzername
        password='Sensid.DB',# Ihr Datenbankpasswort
        database='tooltronic'    # Der Name Ihrer Datenbank
    )
    
    return connection
  except mysql.connector.Error as e:
        print(f"Datenbankverbindungsfehler: {e}", exc_info=True)
        #raise
      