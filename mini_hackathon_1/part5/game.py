from random import *

score = 0
mistake = 0
math_operators = ["+", "-", "*", "/"]
print("== FREAKING MATH CONSOLE ==")
print("Give correct answers to get scores.")
while mistake == 0:
    random_math_operator = choice(math_operators)
    firstNumber = randint(-3, 3)
    secondNumber = randint(1, 3)
    result = randint(-3, 3)
    print('====================')
    print(f"{firstNumber} {random_math_operator} {secondNumber} = {result}")
    print('====================')
    userInput = int(input("1 for True, 0 for False: "))
    print('====================')
    if userInput == 1 and eval(
        str(f"{firstNumber} {random_math_operator} {secondNumber}")
    ) == result:
        score += 1
        print(f'Score: {score}')
        print('####################')

    elif userInput == 0 and eval(
        str(f"{firstNumber} {random_math_operator} {secondNumber}")
    ) != result:
        score += 1
        print(f'Score: {score}')
        print('####################')
    else:
        mistake += 1
print("== GAME OVER ==")
print(f"Your total score is {score}")
