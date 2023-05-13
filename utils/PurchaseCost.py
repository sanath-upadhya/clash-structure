import utils.enum as en

class PurchaseCost:
    elixir:int
    gold:int
    dark_elixir: int
    gems: int
    type_of_resource: str

    def __init__(self, cost, type_of_resource):
        self.type_of_resource = type_of_resource
        self.dark_elixir = 0
        self.elixir = 0
        self.gems = 0
        self.gold = 0
        if type_of_resource == en.ELIXIR:
            self.elixir = cost
        elif type_of_resource == en.GOLD:
            self.gold = cost
        elif type_of_resource == en.DARK_ELIXIR:
            self.dark_elixir = cost
        elif type_of_resource == en.GEMS:
            self.gems = cost
        else:
            print("Wrong type of resource passed!!")

    def get_type_of_resource(self):
        return self.type_of_resource

    def get_cost(self, type_of_resource):
        if type_of_resource == en.ELIXIR:
            return self.elixir
        elif type_of_resource == en.GOLD:
            return self.gold 
        elif type_of_resource == en.DARK_ELIXIR:
            return self.dark_elixir 
        elif type_of_resource == en.GEMS:
            return self.gems
        else:
            return -1


