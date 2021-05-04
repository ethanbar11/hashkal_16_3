import random

# If
x = 5
if x > 5:
    print('Woho')
else:
    print('Bla bli blo')

for i in range(10):
    print(i)

is_done = False
while not is_done:  # is_done==False:
    print('Woho')
    if random.randint(1, 5) > 2:
        is_done = True
