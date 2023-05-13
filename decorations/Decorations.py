from object.Object import Object

class Decorations(Object):
    purchase_cost = {"elixir":0,"gold":0,"gems":0,"dark_elixir":0}
    purchased_by_user = False
    picture = ""

    def __init__(self, size, purchase_cost, picture):
        position = {"x":-1,"y":-1}
        super().__init__(position, size)
        self.purchase_cost = purchase_cost.copy()
        self.picture = picture

    def purchase_decoration(self, position):
        self.position =  position.copy()
        self.purchased_by_user = True

