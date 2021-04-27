import random


def get_random_list(min, max, amount):
    lst = []
    for i in range(amount):
        x = random.randint(min, max)
        lst.append(x)
    return lst


user_input_amount = int(input('Please enter amount: '))
user_input_min = int(input('Please enter minimum: '))
user_input_max = int(input('Please enter maximum: '))
lst = get_random_list(user_input_min, user_input_max, user_input_amount)
print(lst)
