def make_upper(s):
    new_s = ''
    for i in range(len(s)):
        if 97 <= ord(s[i]) <= 122:
            s_as_ascii_int = ord(s[i])
            small_s_as_ascii_int = s_as_ascii_int - 32
            new_s += chr(small_s_as_ascii_int)
        else:
            new_s += s[i]
    return new_s


def make_lower(s):
    new_s = ''
    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90:
            s_as_ascii_int = ord(s[i])
            bigger_s_as_ascii_int = s_as_ascii_int + 32
            new_s += chr(bigger_s_as_ascii_int)
        else:
            new_s += s[i]
    return new_s


def make_lower_upper(s, number):
    if number != 1 and number != 2:
        raise Exception("The number you entered is not 1 or 2!")
    if type(s) != str:
        raise Exception('The string you entered is not valid!')
    if number == 1:
        x = make_lower(s)
        return x
    elif number == 2:
        return make_upper(s)


# make_lower_upper('Ethan', 10)
# make_lower_upper(10, 1)
print(make_lower_upper('Ethan Hello Nice TO MEET you', 1))
# s = 'Hello Ethan1234!'
# new_s = make_upper(s)
# print(new_s)
