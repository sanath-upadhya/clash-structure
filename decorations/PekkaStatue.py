from decorations.Decorations import Decorations

class PekkaStatue(Decorations):

    def __init__(self):
        size = {"length":1, "breadth":1}
        purchase_cost = {"elixir":0,"gold":1000000,"gems":0,"dark_elixir":0}
        picture = "pekka statue picture"
        super().__init__(size, purchase_cost, picture)
        print("Creating pekka statue")