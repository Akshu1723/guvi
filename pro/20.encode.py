akshu=input()
l=[]
for ak in akshu:
    if ak=='X':
        l.append(ord('A'))
    elif ak=='Y':
        l.append(ord('B'))
    elif ak=='Z':
        l.append(ord('C'))
    elif ak=='x':
        l.append(ord('a'))
    elif ak=='y':
        l.append(ord('b'))
    elif ak=='z':
        l.append(ord('c'))
    else:
        l.append(ord(ak)+3)
for ak in l:
    print(chr(ak),end="")
