from buildings.resource.ResourceBuilding import ResourceBuilding
from utils.PurchaseCost import PurchaseCost
from utils.Size import Size
import utils.enum as en

class DarkElixirCollector(ResourceBuilding):

    def __init__(self, number):
        picture = "dark elixir collector"
        self.current_level = 1
        cost = PurchaseCost(en.DE_COLLECTOR_BUILD_COST[self.current_level], en.ELIXIR)
        time = en.DE_COLLECTOR_BUILD_TIME[self.current_level]
        size = Size(2,2)
        hitpoints = en.DE_COLLECTOR_HIT_POINTS[self.current_level]
        type_of_resource = en.DARK_ELIXIR
        super().__init__(size, picture, hitpoints, cost, time, type_of_resource)

        self.unlock_th_level = en.DE_COLLECTOR_TH_AVAILABLE[number]
        self.max_level = 15
        self.max_th_upgrade_level = en.DE_COLLECTOR_MAX_TH_UPGRADE_LEVEL[7]


    def upgrade_town_hall(self, new_th_level):
        super().upgrade_town_hall(new_th_level)

    def upgrade_dark_elixir_collector(self):
        super().upgrade_resource_building()

    def purchase_dark_elixir_collector(self, position):
        super().purchase_building(position)