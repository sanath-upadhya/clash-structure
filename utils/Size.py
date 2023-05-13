class Size:
    length: int
    breadth: int

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_size(self):
        return self.length, self.breadth