# If sentence
x = 5
y = 7
if x > y:
    # Do something
    print('X is bigger than y')
elif x < y:
    print('X is smaller than y.')
else:
    print('X is equal to y.')

# for i in range(10, 1000):
#     print(i)

lst = [1, 5, 12, True, 'Hello']
counter = 0
while lst[counter] != 'Hello':
    # print('This is not the value im looking for:', lst[counter])
    if counter % 2 == 0:
        print('The counter', counter, 'is divided by 2 without shearit')
    counter += 1

print('The value you were looking for is in index number:', counter)


def print_something(num1, num2):
    print('Lets print the numbers:', num1, num2)


print_something(100, 30)
# print('This is after the function')
# Let's print by small characters:
s = 'Hello WORLD!'
print(s.lower())
