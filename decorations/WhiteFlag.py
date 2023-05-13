from decorations.Decorations import Decorations

class WhiteFlag(Decorations):

    def __init__(self):
        size = {"length":1, "breadth":1}
        purchase_cost = {"elixir":5000,"gold":0,"gems":0,"dark_elixir":0}
        picture = "white flag picture"
        super().__init__(size, purchase_cost, picture)
        print("Creating white flag")