list1=['a','d','c','a','b','c']
list1.sort()
print(list1)
delete=[]
lenght=len(list1)-2
for i in range(lenght):
  if list1[i]==list1[i+1]:
    delete.append(i)

print(delete)
