from object.Object import Object
from utils.PurchaseCost import PurchaseCost
from utils.Position import Position

class Building(Object):
    hitpoints: int
    cost: PurchaseCost
    time: int
    unlock_th_level: int
    current_level: int
    max_level: int
    max_th_upgrade_level: int
    created_by_user = False

    def __init__(self, size, picture, hitpoints, purchase_cost, time):
        position = Position(-1,-1)
        super().__init__(position, size, picture)
        self.hitpoints = hitpoints
        self.cost = purchase_cost
        self.time = time

    def purchase_building(self, position):
        self.created_by_user = True
        self.position = position

    def upgrade_building(self):
        if self.current_level < self.max_th_upgrade_level:
            self.current_level = self.current_level + 1
            return True
        else:
            return False
    




