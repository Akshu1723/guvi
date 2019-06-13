a=input()
count=0
for char in a:
    if char.isdigit()==False and char.isalpha()==False and char.isspace()==False:
        count=count+1
print(count)
