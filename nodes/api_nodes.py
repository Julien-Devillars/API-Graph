from NodeGraphQt import BaseNode
import sys
sys.path.append("..")
import requests
import json

from widgets.RunButtonWidgetWrapper import RunButtonWidgetWrapper

class APINode(BaseNode):
    """
    A node class for api
    """

    # unique node identifier.
    __identifier__ = 'API'
    endpoint = ""
    # initial default node name.
    NODE_NAME = 'endpoint'

    def __init__(self):
        super(APINode, self).__init__()

        # create node outputs.
        self.add_output('Success')
        self.add_output('Fail')
        self.hide_widget = True
        self.endpoint = ""
        
        items = ['GET', 'POST', 'UPDATE', 'DELETE']
        self.add_combo_menu('mRequestType', 'Request Type', items=items,
                            tooltip='Type of the request')
        
        run_button = RunButtonWidgetWrapper(self.view)
        self.add_custom_widget(run_button, tab="Custom")
        self.get_widget('mRunButtonWidget').value_changed.connect(self.run)
        
    def run(self):
        request_type = self.get_property("mRequestType")
        
        if(request_type == "GET"):
            response = requests.get(url = self.endpoint)
            data = response.json()
            print(data)
            
        
class APIPokemonNode(APINode):
    """
    A node class for api
    """

    # unique node identifier.
    __identifier__ = 'API'

    # initial default node name.
    NODE_NAME = 'APIPokemon'

    def __init__(self):
        super(APIPokemonNode, self).__init__()
        self.hide_widget = True
        
        self.endpoint += "https://pokeapi.co/api/v2/"
        
class APIPokemon_PokemonNode(APIPokemonNode):
    """
    A node class for api
    """

    # unique node identifier.
    __identifier__ = 'API.Pokemon'

    # initial default node name.
    NODE_NAME = 'Pokemon'

    def __init__(self):
        super(APIPokemon_PokemonNode, self).__init__()
        self.endpoint += "pokemon"
        self.NODE_NAME = self.endpoint

class APIPokemon_ItemNode(APIPokemonNode):
    """
    A node class for api
    """

    # unique node identifier.
    __identifier__ = 'API.Pokemon'

    # initial default node name.
    NODE_NAME = 'Item'

    def __init__(self):
        super(APIPokemon_ItemNode, self).__init__()
        self.endpoint += "item"
        self.NODE_NAME = self.endpoint