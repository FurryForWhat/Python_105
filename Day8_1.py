userName = 'admin'
userPass = '12345'
userEmail = 'admin0123@gmail.com'

user_data = input('Enter name\email:')
if userName == user_data or userEmail == user_data:
    print('Correct login')
    passwd = input('Enter password')
    if userPass == passwd:
        print('Login Success....')
    else:
        print('Incorrect password')
else:
    print('Incorrect login')