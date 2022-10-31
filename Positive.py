list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

for pos in list1:
   if pos > 0:
      print(pos, end = " ")

out2 = [num for num in list2 if num >= 0]
print("\n",out2)
