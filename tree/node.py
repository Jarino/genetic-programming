
class Node():
    def __init__(self, id, value=None, children=None):
        self.id = id
        self.value = value
        self.children = children

    def has_children(self):
        return self.children is not None or len(self.children) != 0
