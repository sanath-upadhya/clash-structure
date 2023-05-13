from decorations.Decorations import Decorations
from utils.Size import Size
from utils.PurchaseCost import PurchaseCost
import utils.enum as en

class WeatherVane(Decorations):

    def __init__(self):
        size = Size(1,1)
        purchase_cost = PurchaseCost(10000, en.ELIXIR)
        picture = "weather vane picture"
        super().__init__(size, purchase_cost, picture)
        print("Creating weather vane")