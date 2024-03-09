from .PokemonBaseNode import PokemonBaseNode

class PokemonNode(PokemonBaseNode):
    """
    A node class for api
    """

    # unique node identifier.
    __identifier__ = 'API.Pokemon'

    # initial default node name.
    NODE_NAME = 'Pokemon'

    def __init__(self):
        super(PokemonNode, self).__init__()
        self.endpoint += "pokemon"
        self.NODE_NAME = self.endpoint

class PokemonNodeId(PokemonBaseNode):
    """
    A node class for api
    """

    # unique node identifier.
    __identifier__ = 'API.Pokemon'

    # initial default node name.
    NODE_NAME = 'PokemonID'

    def __init__(self):
        super(PokemonNodeId, self).__init__()
        self.endpoint += "pokemon/{id}"
        self.NODE_NAME = self.endpoint
        
        self.look_for_endpoint_inputs()