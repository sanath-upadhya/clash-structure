from decorations.Decorations import Decorations

class AncientSkull(Decorations):

    def __init__(self):
        size = {"length":1, "breadth":1}
        purchase_cost = {"elixir":0,"gold":500000,"gems":0,"dark_elixir":0}
        picture = "Ancient skull picture"
        super().__init__(size, purchase_cost, picture)
        print("ancient skull flag")