from decorations.Decorations import Decorations
from utils.Size import Size
from utils.PurchaseCost import PurchaseCost
import utils.enum as en

class SunflowerBed(Decorations):

    def __init__(self):
        size = Size(1,1)
        purchase_cost = PurchaseCost(2500, en.ELIXIR)
        picture = "sunflowerbed picture"
        super().__init__(size, purchase_cost, picture)
        print("Creating SFB")