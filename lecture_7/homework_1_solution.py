def get_words_amount(path):
    counter = 0
    with open(path, 'r') as f:
        # Going over all the lines in the file, each one
        # is one iteration.
        for line in f:
            # Splitting line into words and counting the amount
            # of words in line.
            words_in_line_amount = len(line.split())
            # Adding it to the total counter counting
            # total amount of words in file.
            counter += words_in_line_amount
    return counter

# Reminding you that this is a relative path (read online!)
print(get_words_amount(r'hello.txt'))
