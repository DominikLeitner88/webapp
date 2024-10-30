from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go
from datetime import datetime


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Live_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('site')
    pass
    
  def button_1_click(self, **event_args):
    self.button_1.bold = True
        # Navigieren Sie zur ZielForm
    open_form('site')

  def __init__(self, **properties):
        self.init_components(**properties)
        self.update_plot()
        #result = anvil.server.call('test_db_connection')
        #alert(result)

  def update_plot(self):
        # Daten vom Server abrufen
      try:
        data = anvil.server.call('get_temperature_data')
        timestamps_str = data['timestamps']
        temperatures = data['temperatures']

        # Zeitstempel in datetime-Objekte konvertieren
        timestamps = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in timestamps_str]


        # Diagramm erstellen
        fig = go.Figure(data=go.Scatter(x=timestamps, y=temperatures, mode='lines+markers'))
        fig.update_layout(
          title='Live Temperaturdaten',
          xaxis_title='Zeit',
          yaxis_title='Temperatur (°C)',
          xaxis_tickformat='%Y-%m-%d\n%H:%M:%S'
        )

        self.plot_temperature.figure = fig
      except Exception as e:
          print(f"Fehler beim Aktualisieren des Diagramms: {e}")
          alert(f"Fehler beim Aktualisieren des Diagramms: {e}")
      
        

  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.update_plot()
    pass


