import random

user_choice_str = input('Please enter Hetz/Pali')

user_choice = 0
if user_choice_str == 'Hetz':
    user_choice = 1
elif user_choice_str == 'Pali':
    user_choice = 2
else:
    print('Big Problemo!')

coin = random.randint(1, 2)
if user_choice == coin:
    print('Woho! good guess')
else:
    print('BAD GUESS!')
