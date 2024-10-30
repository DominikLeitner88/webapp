from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go


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
    