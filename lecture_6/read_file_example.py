# Read Example
f = open(r"C:\Users\Borat\PycharmProjects\hashkal_16_3\lecture_6\hello.txt", 'r')
s=''
for l in f:
    s+=l
    # print(l,end='')
print(s)
f.close()
