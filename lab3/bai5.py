default_username = 'admin'
default_password = '123456'
input_username = input('Username: ')
input_password = input('Password: ')
if default_username == input_username and default_password == input_password:
    print(f'You are logged in {default_username}')
else:
    print('Wrong username or password')