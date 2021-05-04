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


s = 'Hello Ethan1234!'
new_s = make_upper(s)
print(new_s)
