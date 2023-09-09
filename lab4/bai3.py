number = int(input('Input number: '))
result = 1
if number > 0:
    for i in range(1, number+1):
        result = result*i
    print(f'{number}! = {result}')
elif number == 0:
    result = 1
    print(f'{number}! = {result}')
else:
    print('Invalid')