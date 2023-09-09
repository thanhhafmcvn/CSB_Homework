a = float(input('Enter the first edge of triangle: '))
b = float(input('Enter the second edge of triangle: '))
c = float( input('Enter the third edge of triangle: '))
if a > 0 and b > 0 and c > 0:
    if a+b>c and a+c>b and b+c>a:
        print(f'The 3 line segments can form an triangle')
    else:
        print(f'The 3 line segments can not form an triangle')
else:
    print('Error.')
