def some_func(num, s):
    if num == 0:
        print(s.lower())
    elif num == 1:
        print(s.upper())


user_input = input('Please enter input: ')
user_choice=int(input('Please enter 0 for small letters and 1 for upper: '))
some_func(user_choice, user_input)
