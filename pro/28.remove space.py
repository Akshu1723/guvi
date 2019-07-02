akshu=list(input())
for ak in akshu:
    if(ak.isspace()):
        akshu.remove(ak)
print("".join(akshu))
