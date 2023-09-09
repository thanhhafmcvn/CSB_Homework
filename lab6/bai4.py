number_of_items = int(input("Number of items: "))
list_of_items = []
order = 1
average = 0
items_above_average_price = []
while order <= number_of_items:
    print("\n")
    item_name = input(f"Item {order}: ")
    price_of_item = float(input("Price of item: "))
    list_of_items.append((item_name, price_of_item))
    order += 1
average = sum(i[1] for i in list_of_items) / len(list_of_items)
items_above_average_price = [i for i in list_of_items if i[1] > average]
print(f"Average price: {average}")
print("Item(s) above average price:", *items_above_average_price)
