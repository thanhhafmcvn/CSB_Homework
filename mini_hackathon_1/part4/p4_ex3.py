print("== Registration ==")

usernameInput = str(input("Username: "))
passwordInput = str(input("Password: "))
confirmPasswordInput = str(input("Confirm password: "))

while passwordInput != confirmPasswordInput:
    print("Invalid passowrd. Please input again")
    confirmPasswordInput = str(input("Confirm password: "))

emailInput = str(input("Email: "))

while "@" not in emailInput or "." not in emailInput:
    print("Invalid email. Please input again")
    emailInput = str(input("Email: "))
    
print("Registered successfully")
