from NodeGraphQt import BaseNode, BaseNodeCircle
import sys
sys.path.append("..")
import json

from widgets.TextLabelWidgetWrapper import TextLabelWidgetWrapper


class APIResponseViewerNode(BaseNode):
    """
    A node class for utils
    """

    # unique node identifier.
    __identifier__ = 'Utils'
    
    # initial default node name.
    NODE_NAME = 'API Response Viewer'

    def __init__(self):
        super(APIResponseViewerNode, self).__init__()

        # create node outputs.
        self.add_input('Json',
                       multi_input = True, 
                       display_name= False)
        #items = ['10', '20', '50', '100']
        #self.add_combo_menu('mNbDisplay', 
        #                    'Number', 
        #                    items=items,
        #                    tooltip='Number of item to display')
        label = TextLabelWidgetWrapper(self.view)
        self.add_custom_widget(label, tab="Custom")
        #self.add_text_input('mResponse', 
        #                    'Response', 
        #                    tab='widgets')
        #self.set_property('mResponse', 
        #                  "test")