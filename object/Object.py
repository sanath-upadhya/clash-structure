from utils.Position import Position
from utils.Size import Size

class Object:
    position: Position
    size: Size
    picture: str

    def __init__(self, position, size, picture):
        self.position = position
        self.size = size
        self.picture = picture

    def move_object(self, new_position):
        self.position = new_position



    

