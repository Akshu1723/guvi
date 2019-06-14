sk=input()
letter_flag = False
number_flag = False
for ak in sk:
  if ak.isalpha():
      letter_flag = True
  if ak.isdigit():
      number_flag = True
if letter_flag and number_flag:
      print('Yes')
else:
  print('No')
