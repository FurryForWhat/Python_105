small_letter = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capter_letter = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol = ['$','#','@']

user_pass = input('Enter password➡️ :')

small_flag = False
capter_flag = False
number_flag = False
symbol_flag = False

if 6 < len(user_pass) < 16:

    for i in user_pass:
        for j in small_letter:
            if i == j:
                small_flag = True

    for i in user_pass:
        for j in capter_letter:
            if i == j:
                capter_flag = True
                
    for i in user_pass:
        for j in number:
            if i == j:
                number_flag = True

    for i in user_pass:
        for j in symbol:
            if i == j:
                symbol_flag = True

    if number_flag == True and small_flag == True and capter_flag == True and symbol_flag == True:
        print('Congratulations, Your password is validate😍😍😍')
    elif number_flag == False or small_flag == False or capter_flag == False or symbol_flag == False:
        print('Your password isn\'t strong enough💩💩💩')
else:
    print('Password must be at least 6 to 16 characters')