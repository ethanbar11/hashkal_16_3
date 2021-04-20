x = int(input('Enter number: '))
if x < 100:
    print('Smaller than 100')
elif 100 <= x < 1000:
    print('Between 100 and 1000')
elif 1000 < x < 2000:
    print('Between 1000 and 2000')
else:
    print('X is not in the spectrum')
