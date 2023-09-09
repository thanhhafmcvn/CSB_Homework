color_list = ["blue", "teal", "green"]
print(*color_list)
item_to_delete = input("Item to delete: ")
try:
    int(item_to_delete)
    color_list.pop(int(item_to_delete) - 1)
    print(*color_list)
except ValueError:
    color_list.remove(item_to_delete)
    print(*color_list)
