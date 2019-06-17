akshu=input()
vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
if any(char in vowels for char in akshu):
    print('yes')
else:
    print('no')
