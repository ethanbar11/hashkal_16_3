def encrypt(s, move_amount):
    new_s = ''
    abc_small = 'abcdefghijklmnopqrstuvwxyz'
    abc_large = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    abc_small_list = list(abc_small)
    abc_large_list = list(abc_large)
    for c in s:
        if c in abc_small_list:
            # finding the position of c in abc_small_list
            index = abc_small_list.index(c)
            # Creating the new index
            new_index = (index + move_amount) % len(abc_small_list)
            new_s += abc_small_list[new_index]
        elif c in abc_large_list:
            index = abc_large_list.index(c)
            new_index = (index + move_amount) % len(abc_large_list)
            new_s += abc_large_list[new_index]
        else:
            new_s += c
    return new_s


def encrypt_file(path, new_path, move_amount):
    s = ''
    with open(path, 'r') as old_file:
        for line in old_file:
            s += line
    encrypted_s = encrypt(s, move_amount)
    with open(new_path, 'w') as new_file:
        new_file.write(encrypted_s)


option = int(input('Please enter 1 for encryption and 2 for decryption : '))
old_path = input('please enter old file name : ')
new_path = input('please enter new- file name : ')
move_amount = int(input('Please enter move amount! : '))
if option == 1:
    encrypt_file(old_path, new_path, move_amount)
elif option == 2:
    encrypt_file(old_path, new_path, -move_amount)
else:
    print('Something is wrong!')
