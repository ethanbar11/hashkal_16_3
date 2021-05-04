# Example 1
# def rasan_function():
#     x = input('Please enter 1 or 2')
#     if x == '1':
#         print('Thank you!')
#         return 'All Good'
#     elif x == '2':
#         print('Double thank you!')
#         return 'All Good'
#     else:
#         return 'Very bad thing happened here'
#
#
# output = rasan_function()
# if output == 'Very bad thing happened here':
#     print('Error happened in Rasan function.')

# Exceptions Example

try:
    print(5 / 1)
except Exception:
    print('There was an error of division by zero.')

try:
    print(5 / 0)
except ZeroDivisionError:
    print('There was an error of division by zero.')

try:
    print(5 / 1)
    print('Hello' + 5)
    print(4 + 7)
except ZeroDivisionError:
    print('There was zero division')
except TypeError:
    print('There was a type error.')

print('Woho')
