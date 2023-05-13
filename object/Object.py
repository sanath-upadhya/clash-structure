class Object:
    position = {"x":-1, "y":-1}
    size = {"length":0, "breadth":0}

    def __init__(self, position, size):
        self.position = position.copy()
        self.size = size.copy()

    def move_object(self, new_position):
        self.position = new_position.copy()



    

