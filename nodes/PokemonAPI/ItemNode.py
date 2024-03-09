from .PokemonBaseNode import PokemonBaseNode

class ItemNode(PokemonBaseNode):
    """
    A node class for api
    """

    # unique node identifier.
    __identifier__ = 'API.Pokemon'

    # initial default node name.
    NODE_NAME = 'Item'

    def __init__(self):
        super(ItemNode, self).__init__()
        self.endpoint += "item"
        self.NODE_NAME = self.endpoint