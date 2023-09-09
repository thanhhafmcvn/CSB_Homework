num = int(input('Type a number: '))
if num%3 == 0 and num%5 == 0:
    print(f'{num} is divisible by 3 and 5')
elif num%3 == 0 and num%5 != 0:
    print(f'{num} is divisible by 3 but not divisible by 5')
elif num%3 != 0 and num%5==0:
    print(f'{num} is divisible by 5 and not divisble by 3')
else:
    print(f'{num} is not divisible by 5 or 3')