minimal = int(input('Please enter min value: '))
maximal = int(input('Please enter max value: '))
if maximal<minimal:
    print('Problem!')
else:
    counter = minimal
    while counter < maximal:
        print(counter)
        counter = counter + 1
