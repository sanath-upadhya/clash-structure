from decorations.Decorations import Decorations

class PointFlag(Decorations):

    def __init__(self):
        size = {"length":1, "breadth":1}
        purchase_cost = {"elixir":15000,"gold":0,"gems":0,"dark_elixir":0}
        picture = "Point flag picture"
        super().__init__(size, purchase_cost, picture)
        print("Creating point flag")