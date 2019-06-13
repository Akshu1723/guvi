a=input()
if any(char.isalpha() for char in a):
    print('No')
elif any(char.isdigit() for char in a):
    print("yes")
