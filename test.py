import decorations as d

position = {"x":2,"y":2}
size = {"length":3, "breadth":3}
purchase_cost = {"elixir":0,"gold":0,"gems":0,"dark_elixir":0}
c = d.Torch()

print(c.size)
print(c.purchase_cost)
print(c.purchased_by_user)
print(c.position)

c.purchase_decoration(position)
print(c.position)
print(c.purchased_by_user)