from NodeGraphQt import BaseNode, BaseNodeCircle, NodeBaseWidget
from Qt import QtCore, QtWidgets

class TextLabelWidgetWrapper(NodeBaseWidget):
    """
    Custom button widget
    """

    def __init__(self, parent=None):
        super(TextLabelWidgetWrapper, self).__init__(parent)
        self.set_name('mLabelWidget')
        self.set_label('Label Widget')
        
        label = QtWidgets.QLabel()
        self.set_custom_widget(label)
        
    def get_value(self):
        return self.get_custom_widget().text()
    
    def set_value(self, value):
        return self.get_custom_widget().setText(value)
        