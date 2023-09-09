number_list = [5, 1, 8, 92, 7, 30]
print("Number list: ", *number_list)
result = [i for i in number_list if i%2==0]
print('Number list with even numbers: ', *result)
