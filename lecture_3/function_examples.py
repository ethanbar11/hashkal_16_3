def add(num1, num2):
    s = num1 + num2
    print('The addition of num1 and num2 is:', s)
    for i in range(1,100):
        print('WOHO IM ALIVE')

    t=50
    if t==50:
        print("MY MONEY IS IN THE BANK")
    return s
    # We are never going to reach here because it's after
    # the return.
    print('woho')


x = add(5, 3)
y = add(9, -503)
print(x)
print(y)
