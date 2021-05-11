# Writing file using relative path.
f = open('a.txt', 'w')
f.write('Bli bla bla\n')
f.write('Kakakakaakakaka')
f.close()

# Method 2 of opening file Using with
with open('a.txt', 'w') as f:
    f.write('Bli bla bla\n')
    f.write('Kakakakaakakaka')

print('The file is closed at this point.')