class Lion:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_bla(self):
        print('My name is : {} and my age is : {}'.format(self.name, self.age))


israel = Lion('Israel', 17)
israel.print_bla()
