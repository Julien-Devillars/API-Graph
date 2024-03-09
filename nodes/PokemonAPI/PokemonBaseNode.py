import sys
sys.path.append("..")

from ..API import APINode

from NodeGraphQt.constants import (
    LayoutDirectionEnum
)

class PokemonBaseNode(APINode):
    """
    A node class for api
    """

    # unique node identifier.
    __identifier__ = 'API'

    # initial default node name.
    NODE_NAME = 'APIPokemon'

    def __init__(self):
        super(PokemonBaseNode, self).__init__()
        self.color = (128, 128, 0, 255)
        self.layout_direction = LayoutDirectionEnum.HORIZONTAL.value
        self.endpoint += "https://pokeapi.co/api/v2/"
        