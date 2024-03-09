#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import signal
import sys

from nodes.PokemonAPI import ItemNode, PokemonBaseNode, PokemonNode
from nodes.Utils import APIResponViewerNode, TextInputNode

native_path = os.path.dirname(os.path.abspath(__file__))

from Qt import QtCore, QtWidgets

from NodeGraphQt import (
    NodeGraph,
    PropertiesBinWidget,
    NodesTreeWidget,
    NodesPaletteWidget
)   

# import example nodes from the "example_nodes" package
from nodes import API
from nodes import API
from nodes.PokemonAPI import PokemonNode, ItemNode


if __name__ == '__main__':
     # handle SIGINT to make the app terminate on CTRL+C
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QtWidgets.QApplication([])

    # create graph controller.
    graph = NodeGraph()

    hotkeys_file =  os.path.join(native_path, "hotkeys", "hotkeys.json")
    
    # set up context menu for the node graph.
    graph.set_context_menu_from_file(hotkeys_file)
    
    # registered example nodes.
    graph.register_nodes([
        PokemonNode.PokemonNode,
        PokemonNode.PokemonNodeId,
        ItemNode.ItemNode,
        APIResponViewerNode.APIResponseViewerNode,
        TextInputNode.TextInputNode
    ])

    # show the node graph widget.
    graph_widget = graph.widget
    graph_widget.resize(1100, 800)
    graph_widget.show()
    
    app.exec_()