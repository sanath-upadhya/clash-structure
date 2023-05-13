from object.Object import Object
from utils.Position import Position
from utils.PurchaseCost import PurchaseCost

class Decorations(Object):
    purchase_cost: PurchaseCost
    purchased_by_user = False

    def __init__(self, size, purchase_cost, picture):
        position = Position(-1, -1)
        super().__init__(position, size, picture)
        self.purchase_cost = purchase_cost

    def purchase_decoration(self, position):
        self.position =  position
        self.purchased_by_user = True

