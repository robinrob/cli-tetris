"""Classes: Element."""

from src.immutable import Immutable


class Element(Immutable):
    """Represents an element of a game object."""

    def __init__(self, type, position=None):
        """Construct an Element of the given ElementType located at the given Position."""
        super(Element, self).__init__(attrs_dict={
            'type': type,
            'position': position
        })
