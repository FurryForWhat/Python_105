import random

random_number = random.randint(1,100)
guess_number = int(input("Enter guessing number within 1 to 100: "))
flag = True
while flag :
    if random_number > guess_number:
        print('Your number is less than random number')
        guess_number = int(input("Enter guessing number within 1 to 100: "))
    elif random_number < guess_number:
        print('Your number is greater than random number')
        guess_number = int(input("Enter guessing number within 1 to 100: "))
    else:
        print('You Win, random number is',random_number)
        flag = False