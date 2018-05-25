class GridSquare:
    def __init__(self):
        self.occupied_by = None

    def __repr__(self):
        if self.is_empty():
            return " "
        else:
            return "*"

    def is_empty(self, ignore_elements=[]):
        return self.occupied_by is None or self.occupied_by in ignore_elements

    def fill_with(self, element):
        self.occupied_by = element

    def clear(self):
        self.occupied_by = None
