with open('hello.txt', 'r') as old_file:
    with open('new_hello.txt', 'w') as new_file:
        for line in old_file:
            new_file.write(line)
        new_file.write('\nThis is a new line that wasnt there before')
