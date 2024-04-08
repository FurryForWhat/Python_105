import random

random_number = random.randint(1,100)
guess_number = int(input("Enter guessing number within 1 to 100: "))
while random_number != guess_number:
    if random_number == guess_number:
        print('You Win')
    else:
        print('You Lose,wrong number')
        guess_number = int(input("Enter guessing number within 1 to 100: "))
print(random_number)