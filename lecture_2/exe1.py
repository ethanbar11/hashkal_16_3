print('You are not going up if your age is less than 8!')

age = int(input('Please enter your age'))
height = float(input('Please enter your height'))

if age >= 8 and age <= 18 and height >= 115:
    print('Woho! You are a kid going on the roller coaster.')
elif age >= 18 and height >= 100:
    print('Woho! You are grown man going on the roller coaster.')
else:
    print('You aint gonna go on no roller coaster')
