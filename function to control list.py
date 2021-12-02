list1=['a','b','c','d','e','f']
list1.append('g')
print(list1)
del list1[3]
print(list1)
list1.pop(3)
print(list1)
for i,j in enumerate(list1):
  print("i:", i, "  j:",j)
