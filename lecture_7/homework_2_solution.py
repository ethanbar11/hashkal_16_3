# I am going to use dictionary (a data structure we learned in the lecture)
# Please make sure you understand it before reading the solution.
def count_word_frequency(path):
    with open(path, 'r') as f:
        # Creating a new empty dictionary
        frequencies = {}
        # Going over all the lines
        for line in f:
            # The split function returns a list (words is a list)
            words = line.split()
            for word in words:
                # If a certain word is a key in the dictionary
                if word not in frequencies:
                    frequencies[word] = 1
                else:
                    frequencies[word] += 1
        return frequencies


print(count_word_frequency('hello.txt'))
