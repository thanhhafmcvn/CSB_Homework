a = 0
b = 1
result = []
number = int(input('Input a positive number: '))
for i in range(number):
    result.append(str(b))
    c = a + b
    a = b
    b = c
print(f'First {number} of Fibonacci number(s): {" ".join(result)}')