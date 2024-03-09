from NodeGraphQt import BaseNode
import sys
sys.path.append("..")
import requests
import json

from widgets.RunButtonWidgetWrapper import RunButtonWidgetWrapper

from NodeGraphQt.constants import (
    LayoutDirectionEnum,
    NodePropWidgetEnum,
    PipeLayoutEnum
)

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
        self.endpoint = ""
        
        items = ['GET', 'POST', 'UPDATE', 'DELETE']
        self.add_combo_menu('mRequestType', 'Request Type', items=items,
                            tooltip='Type of the request')
        
        run_button = RunButtonWidgetWrapper(self.view)
        self.add_custom_widget(run_button, tab="Custom")
        
        self.add_text_input("mPostBodyRequest", "Body Request")
        self.hide_widget("mPostBodyRequest", False)
        
        self.get_widget('mRunButtonWidget').value_changed.connect(self.run)
        self.get_widget('mRequestType').value_changed.connect(
            lambda k, cb_value: self.display_post_data(cb_value))
        
    def run(self):
        request_type = self.get_property("mRequestType")
        
        if(request_type == "GET"):
            response = requests.get(url = self.endpoint)
            data = response.json()
        
        ports = self.connected_output_nodes()
        for port_key in ports:
            for connected_node in ports[port_key]:
                connected_node.set_property('mLabelWidget', json.dumps(data, indent=4))
                connected_node.update_model()
                connected_node.view.draw_node()
    
    def display_post_data(self, request_type):
        if request_type == "POST" or request_type == "UPDATE":
            self.show_widget("mPostBodyRequest", False)
        else:
            self.hide_widget("mPostBodyRequest", False)
  