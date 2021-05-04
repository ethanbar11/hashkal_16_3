def get_number():
    is_valid = False
    x = 0
    while not is_valid:
        try:
            x = int(input('Please enter a number: '))
            is_valid = True
        except Exception:
            print('The input is not a number!')
            is_valid = False
    return x

print(get_number())
