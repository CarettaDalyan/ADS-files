#Basic set operations
#Chrissie 22/11/2020
#see also https://www.tutorialspoint.com/python-set-operation

set1 = { "Pumpkin", 90210, True, (255, 197, 69) }
set2 = { "Pasta", 90210, 'cz', 12.24, "Pumpkin"}

print (set1.difference(set2))
print (set1.intersection(set2))
print (set1.union(set2))

print ("Pasta" in set1)
print ("Pasta" in set2)
for element in set2:
    print (element)



