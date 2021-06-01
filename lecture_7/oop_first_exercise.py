class Lion:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_bla(self):
        print('My name is : {} and my age is : {}'.format(self.name, self.age))


class Zoo:
    def __init__(self):
        self.lions = []

    def add_lion(self, name, age):
        lion = Lion(name, age)
        self.lions.append(lion)

    def remove_lion(self, name):
        is_found_lion = False
        index_of_lion = -1
        for i in range(len(self.lions)):
            if self.lions[i].name == name:
                is_found_lion = True
                index_of_lion = i
        if is_found_lion:
            del self.lions[index_of_lion]

    def print_lion_amount(self):
        print(len(self.lions))


# israel = Lion('Israel', 17)
# israel.print_bla()

zoo = Zoo()
zoo.add_lion('Ethan', 25)
zoo.add_lion('Woho', 30)
zoo.add_lion('Python', 70)
zoo.add_lion('Bla ', 1)
zoo.print_lion_amount()
zoo.remove_lion('Woho')
zoo.print_lion_amount()
