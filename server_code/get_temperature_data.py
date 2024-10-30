import anvil.server
from anvil.server import callable
from .get_mysql import get_db_connection
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
@anvil.server.callable
def get_temperature_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DATE_FORMAT(TIMESTAMP, '%Y-%m-%d %H:%i:%S'),sensorValue1 FROM tooltronic.measurement ORDER BY timestamp desc LIMIT 100")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    # Daten in ein geeignetes Format konvertieren
    timestamps = [row[0] for row in data]
    temperatures = [row[1] for row in data]
    return {'timestamps': timestamps, 'temperatures': temperatures}