from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go
from datetime import datetime

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.last_timestamp = None  # Letzten Zeitstempel speichern
    self.timestamps = []
    self.temperatures = []
    self.update_plot()
    # Any code you write here will run before the form opens.

  def Live_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('site')
    pass
    
  def button_1_click(self, **event_args):
    self.button_1.bold = True
        # Navigieren Sie zur ZielForm
    open_form('site')

  #def __init__(self, **properties):
        #self.init_components(**properties)
        #self.update_plot()
        #result = anvil.server.call('test_db_connection')
        #alert(result)

  def update_plot(self):
    try:
        data = anvil.server.call('get_new_temperature_data', self.last_timestamp)
        new_timestamps_str = data['timestamps']
        new_temperatures = data['temperatures']

        if new_timestamps_str and new_temperatures:
            # Neue Daten verarbeiten
            new_timestamps = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in new_timestamps_str]

            # Daten anhängen
            self.timestamps.extend(new_timestamps)
            self.temperatures.extend(new_temperatures)

            # Letzten Zeitstempel aktualisieren
            self.last_timestamp = new_timestamps_str[-1]

            # Diagramm aktualisieren
            self.update_plot_data()
    except Exception as e:
        print(f"Fehler beim Aktualisieren des Diagramms: {e}")
        alert("Ein Fehler ist aufgetreten. Bitte versuchen Sie es später erneut.")

  def update_plot_data(self):
    # Diagramm aktualisieren, ohne es neu zu erstellen
    if not hasattr(self, 'fig'):
        # Wenn das Diagramm noch nicht existiert, erstellen
        self.fig = go.Figure()
        self.fig.add_trace(go.Scatter(x=self.timestamps, y=self.temperatures, mode='lines+markers'))
        self.fig.update_layout(
            title='Live Temperaturdaten',
            xaxis_title='Zeit',
            yaxis_title='Temperatur (°C)',
            xaxis_tickformat='%Y-%m-%d\n%H:%M:%S'
        )
        self.plot_temperature.figure = self.fig
    else:
        # Daten im bestehenden Diagramm aktualisieren
        self.fig.data[0].x = self.timestamps
        self.fig.data[0].y = self.temperatures
        self.plot_temperature.figure = self.fig
      
        

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.update_plot()
    pass


