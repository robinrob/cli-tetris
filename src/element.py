from src.immutable import Immutable


class Element(Immutable):
    def __init__(self, type, position=None):
        super(Element, self).__init__(attrs_dict={
            'type': type,
            'position': position
        })
