class Human:
    def __init__(self, name, height):
        self.my_name = name
        self.my_my_height = height

    def print_my_attributes(self):
        print('My name is', self.my_name, 'and my height is', self.my_my_height)


class School:
    def __init__(self):
        self.students = []

    def add_student(self, name, height):
        # Creating new human object from the params received.
        student = Human(name, height)
        # Appending it to the list (which is unique to each object created from the class!)
        self.students.append(student)

    def print_all_students(self):
        # going over all students in class and printing them.
        for student in self.students:
            print('Student name : {} height : {}'.format(student.my_name, student.my_my_height))


# Creating new object
# ethan = Human('Ethan', 178)
# ethan.print_my_attributes()
#
# ofek = Human('Ofek', 185)
# ofek.print_my_attributes()


# Creating school and using it.
school = School()
school.add_student('Hadas', 170)
school.add_student('Israel', 168)
school.add_student('Itzhak', 178)
school.print_all_students()
