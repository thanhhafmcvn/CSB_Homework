months_with_31days = [1,3,5,7,8,10,12]
months_with_30days = [4,6,9,11]
special_month = [2]
userInput = int(input('Input a month: '))
if userInput in months_with_31days:
    print('This month has 31 days')
elif userInput in months_with_30days:
    print('This month has 30 days')
elif userInput in special_month:
    print('This month has 28 or 29 days')
else:
    print('Invalid input')