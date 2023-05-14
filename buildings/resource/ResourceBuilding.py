from buildings.Building import Building
from utils.PurchaseCost import PurchaseCost
import utils.enum as en

class ResourceBuilding(Building):
    production_capacity: int
    storage_capacity: int
    type_of_resource: str

    def __init__(self, size, picture, hitpoints, purchase_cost, time, type_of_resource):
        self.type_of_resource = type_of_resource
        self.set_storage_capacity()
        self.set_production_capacity()
        super().__init__(size, picture, hitpoints, purchase_cost, time)

    def set_storage_capacity(self):
        if self.type_of_resource == en.GOLD or self.type_of_resource == en.ELIXIR:
            self.storage_capacity = en.GE_COLLECTOR_STORAGE_CAPACITY[self.current_level]
        elif self.type_of_resource == en.DARK_ELIXIR:
            self.storage_capacity = en.DE_COLLECTOR_STORAGE_CAPACITY[self.current_level]

    def set_production_capacity(self):
        if self.type_of_resource == en.GOLD or self.type_of_resource == en.ELIXIR:
            self.production_capacity = en.GE_COLLECTOR_PRODUCTION_CAPCAITY[self.current_level]
        elif self.type_of_resource == en.DARK_ELIXIR:
            self.production_capacity = en.DE_COLLECTOR_PRODUCTION_CAPCAITY[self.current_level]

    def set_next_values(self):
        level = self.current_level
        if self.type_of_resource == en.GOLD or self.type_of_resource == en.ELIXIR:
            self.storage_capacity = en.GE_COLLECTOR_STORAGE_CAPACITY[level]
            self.production_capacity = en.GE_COLLECTOR_PRODUCTION_CAPCAITY[level]
            self.cost.set_cost(en.GE_COLLECTOR_BUILD_COST[level])
            self.time = en.GE_COLLECTOR_BUILD_TIME[level]
            self.hitpoints = en.GE_COLLECTOR_HIT_POINTS[level]
        elif self.type_of_resource == en.DARK_ELIXIR:
            self.storage_capacity = en.DE_COLLECTOR_STORAGE_CAPACITY[level]
            self.production_capacity = en.DE_COLLECTOR_PRODUCTION_CAPCAITY[level]
            self.cost.set_cost(en.DE_COLLECTOR_BUILD_COST[level])
            self.time = en.DE_COLLECTOR_BUILD_TIME[level]
            self.hitpoints = en.DE_COLLECTOR_HIT_POINTS[level]   

    def upgrade_resource_building(self):
        #check if max upgrade level for TH reached
        if super().upgrade_building():
            self.set_next_values()
        else:
            print("Max level for TH reached")

    def upgrade_town_hall(self, new_th_level):
        if self.type_of_resource == en.GOLD or self.type_of_resource == en.ELIXIR:
            self.max_th_upgrade_level = en.GE_COLLECTOR_MAX_TH_UPGRADE_LEVEL[new_th_level]
        elif self.type_of_resource == en.DARK_ELIXIR:
            self.max_th_upgrade_level = en.DE_COLLECTOR_MAX_TH_UPGRADE_LEVEL[new_th_level]

    def set_next_cost(self,cost,time):
        if self.type_of_resource == en.GOLD or self.type_of_resource == en.ELIXIR:
            self.cost.set_cost(en.GE_COLLECTOR_BUILD_COST[self.current_level])
            self.time = en.GE_COLLECTOR_BUILD_TIME[self.current_level]
        elif self.type_of_resource == en.DARK_ELIXIR:
            self.cost.set_cost(en.DE_COLLECTOR_BUILD_COST[self.current_level])
            self.time = en.DE_COLLECTOR_BUILD_TIME[self.current_level] 

    def purchase_building(self, position):
        super().purchase_building(position)

