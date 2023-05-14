import decorations as d
from utils.Position import Position
from utils.Size import Size
import utils.enum as en
from buildings.resource.DarkElixirCollector import DarkElixirCollector

position = Position(2,2)
size = Size(2,2)
gc = DarkElixirCollector(1)

print(gc.cost.get_cost(en.ELIXIR))
print(gc.picture)
gc.upgrade_dark_elixir_collector()
print(gc.storage_capacity)
gc.upgrade_dark_elixir_collector()
print(gc.storage_capacity)
gc.upgrade_dark_elixir_collector()


# print(c.size)
# type_of_resource = c.purchase_cost.get_type_of_resource()
# print(c.purchase_cost.get_type_of_resource())
# print(c.purchase_cost.get_cost(type_of_resource))
# print(c.purchased_by_user)
# print(str(c.position.x) + str(c.position.y))

# c.purchase_decoration(position)
# print(str(c.position.x) + str(c.position.y))
# print(c.purchased_by_user)