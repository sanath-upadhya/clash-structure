from decorations.Decorations import Decorations
from utils.Size import Size
from utils.PurchaseCost import PurchaseCost
import utils.enum as en

class PirateFlag(Decorations):

    def __init__(self):
        size = Size(1,1)
        purchase_cost = PurchaseCost(500, en.GEMS)
        picture = "Pirate flag picture"
        super().__init__(size, purchase_cost, picture)
        print("pirate flag")