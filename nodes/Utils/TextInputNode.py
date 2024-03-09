from NodeGraphQt import BaseNode
import sys
sys.path.append("..")
sys.path.append("../..")

from widgets.TextLabelWidgetWrapper import TextLabelWidgetWrapper

class TextInputNode(BaseNode):
    """
    A node class for utils
    """

    # unique node identifier.
    __identifier__ = 'Utils'
    
    # initial default node name.
    NODE_NAME = 'Text input'

    def __init__(self):
        super(TextInputNode, self).__init__()

        # create node outputs.
        self.add_output("mTextOutput", display_name=False)
        
        self.color = (128, 128, 128, 255)
        self.add_text_input("mText")
    
    def getText(self):
        return self.get_property("mText")