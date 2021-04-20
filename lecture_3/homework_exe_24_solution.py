small_vowels = ['a', 'e', 'i', 'o', 'u', 'y']

s = input('Please enter a letter : ')
s = s.lower()
i = 0
is_found_letter = False
while i < len(small_vowels):
    if small_vowels[i] == s:
        is_found_letter = True
    i += 1

if is_found_letter == True:
    print('This is a vowel!')

else:
    print('This is NOT NOT NOT NOT a vowel')
