is_valid = False
while is_valid == False:
    x = int(input('Please enter a **valid** number'))
    if x < 100:
        print('Number is too low!')
    elif x > 350:
        print('Number is too big!')
    elif x % 2 == 0:
        print('You should enter an odd number!')
    else:
        is_valid = True
print('The valid number you entered is :', x)
