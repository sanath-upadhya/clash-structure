from decorations.Decorations import Decorations

class Torch(Decorations):

    def __init__(self):
        size = {"length":1, "breadth":1}
        purchase_cost = {"elixir":500,"gold":0,"gems":0,"dark_elixir":0}
        picture = "torch picture"
        super().__init__(size, purchase_cost, picture)
        print("Creating torch")

    
