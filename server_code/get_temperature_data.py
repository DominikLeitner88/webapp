import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
@anvil.server.callable
def get_temperature_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT TIMESTAMP,sensorValue1 FROM tooltronic.measurement ORDER BY timestamp DESC LIMIT 100")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    # Daten in ein geeignetes Format konvertieren
    timestamps = [row[0] for row in data]
    temperatures = [row[1] for row in data]
    return {'timestamps': timestamps, 'temperatures': temperatures}