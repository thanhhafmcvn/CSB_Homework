color_list = ["blue",  "teal", "green"]
print("Color list: ", *color_list)
color_list.append(str(input('Input a new color: ')))
print("Updated list: ", *color_list)
