number_list = []
print('Enter 0 to finish')
while True:
   user_input = int(input())
   if user_input == 0:
      break
   number_list.append(user_input) 

print(f'Sum of numbers in list: {sum(number_list)}')