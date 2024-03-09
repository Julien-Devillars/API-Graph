from NodeGraphQt import BaseNode, BaseNodeCircle, NodeBaseWidget
from Qt import QtCore, QtWidgets

class RunButtonWidgetWrapper(NodeBaseWidget):
    """
    Custom button widget
    """

    def __init__(self, parent=None):
        super(RunButtonWidgetWrapper, self).__init__(parent)
        self.set_name('mRunButtonWidget')
        self.set_label('Run Button Widget')
        
        run_button = QtWidgets.QPushButton('Run')
        run_button.setToolTip("Run the API")
        run_button.clicked.connect(self.on_value_changed)
        
        self.set_custom_widget(run_button)
        
    def get_value(self):
        return 0
    
    def set_value(self, value):
        return value
        