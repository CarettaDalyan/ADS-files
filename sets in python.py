basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit = set(basket)               # create a set without duplicates
print (fruit)


print ('orange' in fruit)                # fast membership testing

print ('crabgrass' in fruit)


 # Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print a                                  # unique letters in a

print a - b                              # letters in a but not in b

print a | b                              # letters in either a or b

print a & b                              # letters in both a and b

print a ^ b                              # letters in a or b but not both
