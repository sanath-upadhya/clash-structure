from buildings.Building import Building
from utils.Position import Position
from utils.Size import Size
from utils.PurchaseCost import PurchaseCost
import utils.enum as en

class BuilderHut(Building):

    def __init__(self, number):
        position = Position(-1,-1)
        picture = "Builder hut picture"
        size = Size(1, 1)
        hitpoints = 250
        purchase_cost = PurchaseCost(en.BUILDER_HUT_COST[number],en.GEMS)
        time = 0
        super().__init__(size, picture, hitpoints, purchase_cost, time)

        self.current_level = 1
        self.max_level = 1
        self.max_th_upgrade_level = 1
        self.unlock_th_level = 1

    def purchase_builder_hut(self, position):
        super().purchase_building(position)
    


