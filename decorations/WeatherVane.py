from decorations.Decorations import Decorations

class WeatherVane(Decorations):

    def __init__(self):
        size = {"length":1, "breadth":1}
        purchase_cost = {"elixir":10000,"gold":0,"gems":0,"dark_elixir":0}
        picture = "weather vane picture"
        super().__init__(size, purchase_cost, picture)
        print("Creating weather vane")