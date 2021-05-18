class Human:
    def __init__(self, name, height):
        self.my_name = name
        self.my_my_height = height

    def print_my_attributes(self):
        print('My name is', self.my_name, 'and my height is', self.my_my_height)

# Creating new object
ethan = Human('Ethan', 178)
ethan.print_my_attributes()

ofek = Human('Ofek', 185)
ofek.print_my_attributes()
