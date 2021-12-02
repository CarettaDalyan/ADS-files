# simple test functions
#chrissie 22/11/2020

def simplehash(stringval):
    sh = sum(map(ord, stringval))
    return sh

def betterhash(stringval):
        multiplier = 1
        hashval = 0
        for char in stringval:
            hashval += multiplier * ord(char)
            multiplier += 1
        return hashval

for i in range (0, 2):
    stringval = input("Enter a string >> ")
    print (betterhash(stringval))

