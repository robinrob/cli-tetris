from src.element_type import ElementType

class GridSquare:
    def __init__(self):
        self._occupied_by = None

    def __repr__(self):
        if self.is_empty():
            return " "
        else:
            return "*"

    def is_empty(self):
        return self._occupied_by is None

    def fill_with(self, element):
        self._occupied_by = element.type

    def clear(self):
        self._occupied_by = None
