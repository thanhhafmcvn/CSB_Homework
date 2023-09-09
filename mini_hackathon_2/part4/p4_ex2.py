number_list = []
print('Enter 0 to finish')
while True:
    number_list.append(int(input()))
    if 0 in number_list:
        number_list.remove(0)
        break
result = [i for i in number_list if i % 2 == 0]
print(f'Even number in list: {result}')