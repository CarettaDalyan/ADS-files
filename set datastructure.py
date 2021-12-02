a=set()
b=set('238764')
print(b)
b.add("23")
b.remove('2')
print(len(b))
print(b)

list1=[2,3,7,6]
list2=[6,7,8,9]
d=set(list1)
e=set(list2)

print("d :",d)
print("e :",e)
union=e|d
print("union :", union)
intersection = e &d
print("intersection :", intersection)
difference=e-d
print("difference: ",difference)
symdif=e^d
print("symdif: ",symdif)

