userInput = input('Enter a character: ')
try:
    int(userInput)
    print(f'{userInput} is a digit')
except ValueError:
    print(f'{userInput} is not a digit')

