# Exercises Solutions
# 1PracticePython Question 4

number = int(input('Please enter a number!'))

divisor = 1
lst = []
while divisor <= number:
    if number % divisor == 0:
        # This line is telling lst (the list) to add the variable
        # number to itself.
        print('The number', divisor, 'is a divisor of', number)
        lst.append(divisor)
    else:
        print('The number', divisor, 'is not a divisor of', number)
    divisor += 1

print(lst)
