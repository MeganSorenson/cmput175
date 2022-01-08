# Exercise 1: Python Warm Up
# a program for Bluebell Greenhouses that prints a purchase receipt

# Part 1
#   dict representing the spring flower bulbs (keys) sold and their price per bulb (values)
#   price per bulb is in dollars and is float type
#   bulb type is type str
bulbs_for_sale = {
    'daffodil': 0.35,
    'tulip': 0.33,
    'crocus': 0.25,
    'hyacinth': 0.75,
    'bluebell': 0.50
}

# Part 2
#   dict representing mary's annual standing order
#   keys are the bulb types and are type str
#   values are the number of bulbs in the order and are type int
mary_order = {
    'daffodil': 50,
    'tulip': 100
}

# Part 3
#   updating price of tulips due to high demand (rounded to 2 decimal places)
#   price has increased by 25%
price_increase = 1.25
bulbs_for_sale['tulip'] = float("%2.2f" % (
    bulbs_for_sale['tulip'] * price_increase))

# Part 4
#  updating mary's order to add hyacinths
mary_order['hyacinth'] = 30

# Part 5
#   display may's order as a receipt
#   in order bulb code, number of bulbs, and subtotal
#   bulb code (str of first three letters in caps) is left aligned with field width 5
#   number of bulbs is an int with field width 4 and right aligned
#   subtotal is a float with field width 6, right aligned, and 2 decimal places
#   bulb codes are sorted alphabetically
sold_bulbs = []
# add bulbs to list to order alphabetically
for bulb in mary_order.keys():
    sold_bulbs.append(bulb)
sold_bulbs.sort()

# print receipt
print("You have purchased the following bulbs:")
for bulb in sold_bulbs:
    print("%-5s * %4i = $ %6.2f" % (bulb.upper()
          [0:3], mary_order[bulb], mary_order[bulb] * bulbs_for_sale[bulb]))

# Part 6
#   calculate total number of bulbs mary ordered
#   calculate total cost of order
#   total cost is a float that is right aligned, field width 6, 2 decimal places
total_cost = 0
# get total amoutn spent using mary_order and bulbs_for_sale dictionaries
for bulb, amount in mary_order.items():
    total_cost += amount * bulbs_for_sale[bulb]

print("Thank you for purchasing %i bulbs from Bluebell Greenhouses." %
      (sum(mary_order.values())))
print("Your total comes to $ %6.2f." % (total_cost))
