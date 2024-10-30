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
from .get_mysql import get_db_connection
@anvil.server.callable
def test_db_connection():
    try:
        conn = get_db_connection()
        conn.close()
        return "Verbindung erfolgreich"
    except Exception as e:
        return f"Verbindungsfehler: {e}"