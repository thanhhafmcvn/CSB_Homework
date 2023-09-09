print('== Registration ==')
usernameInput = str(input('Username: '))
passwordInput = str(input('Password: '))
confirmPasswordInput = str(input('Confirm password: '))
while passwordInput != confirmPasswordInput:
    print('Invalid passowrd, please input again')
    confirmPasswordInput = str(input('Confirm password: '))
emailInput = str(input('Email: '))
print('Registered successfully')