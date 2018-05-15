from src.element_type import ElementType

class GridSquare:
    def __init__(self):
        self._occupied_by = None

    def __repr__(self):
        if self.is_empty():
            return " "
        else:
            return "*"

    def is_empty(self, ignore_elements=[]):
        return self._occupied_by is None or self._occupied_by in ignore_elements

    def fill_with(self, element):
        self._occupied_by = element

    def clear(self):
        self._occupied_by = None
