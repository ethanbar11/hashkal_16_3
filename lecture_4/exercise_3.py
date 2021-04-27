import random


def guessing_game():
    number = random.randint(1, 10)
    is_guessed_right = False
    while is_guessed_right != True:
        x = int(input('Please enter number: '))
        if x == number:
            print('You guessed right mister!')
            is_guessed_right = True
        else:
            print('You guessed wrong buddy.')


def guessing_game_v2():
    number = random.randint(1, 10)
    x = int(input('Please enter number: '))
    while x != number:
        print('You entered a wrong number!')
        x = int(input('Please enter another number: '))
    print('You guessed the right number: ',x,'very good job!')


guessing_game_v2()
