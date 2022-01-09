# Exercise 1: Python Warm Up
# a program for Bluebell Greenhouses that prints a purchase receipt for customers
# uses mary's annual order as an example

def create_sale_dictionary():
    # creates a dict representing the spring flower bulbs (keys) sold and their price per bulb (values)
    # price per bulb is in dollars and is float type
    # bulb type is type str
    # returns this described dictionary
    bulbs_for_sale = {
        'daffodil': 0.35,
        'tulip': 0.33,
        'crocus': 0.25,
        'hyacinth': 0.75,
        'bluebell': 0.50
    }
    return bulbs_for_sale


def create_order(customer_name):
    # creates a dict representing a customer's annual standing order
    # keys are the bulb types and are type str
    # values are the number of bulbs in the order and are type int
    # customer name is a str representing which customer is being serviced
    # returns the described dictionary
    if customer_name == 'Mary':
        order = {
            'daffodil': 50,
            'tulip': 100
        }
    else:
        order = {}
    return order


def update_price(bulb_type, price_increase, bulbs_for_sale):
    # updating price of a bulb typedue to high demand (rounded to 2 decimal places)
    # bulb_type is a string representing which bulb type's rice is being changed
    # price increase is a float representing the overall increase in price
    # bulbs_for sale is a dictionary of bulb_type : price that is being updated
    # returns NoneType
    bulbs_for_sale[bulb_type] = float("%2.2f" % (
        bulbs_for_sale[bulb_type] * price_increase))


def add_to_order(customer_order, bulb_type, quantity):
    # updates a customer's order
    # customer_order is a dictionary of bulb : quantity representing a customer's order
    # bulb_type is a str represetning the type of bulb to be added
    # quantity is an int representing the number of bulbs to be added
    # returns NoneType
    customer_order[bulb_type] = quantity


def print_receipt(customer_order, bulbs_for_sale):
    # displays customer's order as a receipt
    # in order bulb code, number of bulbs, and subtotal
    # bulb codes are sorted alphabetically
    # customer_order is a dictionary of bulb : quantity representing a customer's order
    # bulbs_for_sale is a dictionary of bulb : price representing the bulbs per sale
    # returns NoneType
    sold_bulbs = []
    # add bulbs to list to order alphabetically
    for bulb in customer_order.keys():
        sold_bulbs.append(bulb)
    sold_bulbs.sort()

    # print receipt;
    #   bulb code (str of first three letters in caps) is left aligned with field width 5
    #   number of bulbs is an int with field width 4 and right aligned
    #   subtotal is a float with field width 6, right aligned, and 2 decimal places
    print("You have purchased the following bulbs:")
    for bulb in sold_bulbs:
        print("%-5s * %4i = $ %6.2f" % (bulb.upper()
                                        [0:3], customer_order[bulb], customer_order[bulb] * bulbs_for_sale[bulb]))


def print_total(customer_order, bulbs_for_sale):
    # calculates and displays total number of bulbs a customer ordered and total cost of order
    # customer_order is a dictionary of bulb : quantity representing a customer's order
    # bulbs_for_sale is a dictionary of bulb : price representing the bulbs per sale
    # returns NoneType
    total_cost = 0
    # get total amount spent using mary_order and bulbs_for_sale dictionaries
    for bulb, amount in customer_order.items():
        total_cost += amount * bulbs_for_sale[bulb]
    # print totals;
    #   total cost is a float that is right aligned, field width 6, 2 decimal places
    print()
    print("Thank you for purchasing %i bulbs from Bluebell Greenhouses." %
          (sum(customer_order.values())))
    print("Your total comes to $ %6.2f." % (total_cost))


def main():
    # Part 1: create dictionary of bulbs for sale
    bulbs_for_sale = create_sale_dictionary()

    # Part 2: create customer order
    customer_name = 'Mary'
    mary_order = create_order(customer_name)

    # Part 3: update price based on price increase
    price_increase = 1.25
    updated_bulb_type = 'tulip'
    update_price(updated_bulb_type, price_increase, bulbs_for_sale)

    # Part 4: updating mary's order
    added_bulb_type = 'hyacinth'
    added_quantity = 30
    add_to_order(mary_order, added_bulb_type, added_quantity)

    # Part 5: display customer order as receipt
    print_receipt(mary_order, bulbs_for_sale)

    # Part 6: calculate and display totals of order
    print_total(mary_order, bulbs_for_sale)


main()
