number_list = [5, 1, 8, 92, -1, 30]
user_input = int(input('Input a number: '))
result = [print(f'Number found at position: {number_list.index(user_input)+1}') if user_input in number_list else print('Number not found')]
