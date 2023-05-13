from decorations.Decorations import Decorations

class MightyHeroStatue(Decorations):

    def __init__(self):
        size = {"length":1, "breadth":1}
        purchase_cost = {"elixir":0,"gold":0,"gems":500,"dark_elixir":0}
        picture = "Mighty hero statue picture"
        super().__init__(size, purchase_cost, picture)
        print("creating mighty hero statue")