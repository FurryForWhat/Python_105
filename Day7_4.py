user_name = 'admin'
user_password = 'admin007'
user_email = 'admin@gmail.com'


input_username = input('Enter username :')

if user_name == input_username:
    print('user name is correct')
    input_userpass = input('Enter password :')
    if input_userpass == user_password:
        print('Login Success....')
    else:
        print('Wrong password')
else:
    print('user name is wrong')

#empty string
#email checking