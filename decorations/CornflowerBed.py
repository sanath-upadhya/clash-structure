from decorations.Decorations import Decorations

class CornflowerBed(Decorations):

    def __init__(self):
        size = {"length":1, "breadth":1}
        purchase_cost = {"elixir":2500,"gold":0,"gems":0,"dark_elixir":0}
        picture = "cornflower picture"
        super().__init__(size, purchase_cost, picture)
        print("Creating CFB")