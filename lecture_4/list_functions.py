# Example with len()
lst = ['Hello', 'Every', 'Body', 1]
for i in range(len(lst)):
    print(i + 1, lst[i])

# Appending to list
print('List before:', lst)
lst.append('Ethan')
print('List after:', lst)

# Summing 2 list
lst2 = ['woho', 123, 50]
lst3 = lst + lst2
print(lst3)

# Count:
lst4 = [1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 1]
print(lst4.count(1))

# Clear:
print('List before:', lst4)
lst4.clear()
print('List after:', lst4)

# Reverse
print('List before:', lst3)
lst3.reverse()
print('List after:', lst3)

# Sort:
numbers_lst = [412, 423, 44, 4, 2, 3, 5, 5, 32, 4, 43412]
print('List before:', numbers_lst)
numbers_lst.sort()
print('List after:', numbers_lst)

# in
if 44 in numbers_lst:
    print('Woho!')
else:
    print('44 is not in the lst.')
