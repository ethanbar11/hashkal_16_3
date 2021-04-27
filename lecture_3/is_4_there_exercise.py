# First option


# count = 0
# for i in range(len(lst)):
#     if lst[i] == 4:
#         count += 1
#
# print('The amount of 4\'s in lst is',count)

# Second option (with function)

def get_number_of_4s(l):
    count = 0
    for i in range(len(l)):
        if l[i] == 4:
            count += 1
    return count

lst = [1, 4, 3214, 1, 234, 1243, 4, 23, 4, 4, 3, 4, 3, 43, 4, 3, 4, 65, 1, 54]

x=get_number_of_4s(lst)
print('Number of 4s is:',x)