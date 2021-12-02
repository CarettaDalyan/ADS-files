#a simple hash table based on a list
#you can set the size to whatever you want
#Chrissie 22/11/2020

#start with hashitem that will go in the hashtable
#it needs both a key and a value
class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

#now make the table itself, size can be set using a parameter
class HashTable:
    def __init__(self, size):
        self.size = size
        #create empty slots
        self.slots = [None for i in range(self.size)]
        #and initialise the count (actual items) to 0
        self.count = 0

    def _hash(self, key):
        #hash the items using a multiplier
        #this method name starts with a _ as it is meant to be a private method
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        #print (str(hv)) #- uncomment this to see the individual hash values
        return hv % self.size

    def put(self, key, value):
        #add new item to the hashtable
        item = HashItem(key, value)
        h = self._hash(key)
        #use next available slot
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h + 1) % self.size
        if self.slots[h] is None:
            self.count += 1
        self.slots[h] = item

    def get(self, key):
        #get the value requested by the key
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h+ 1) % self.size
        #and return none if not found
        return None

    def __setitem__(self, key, value):
        #this method starts uses __ and is called a dunder method
        #it is a method that can be invoked without an explicit call
        #another example is  __init__
        #these are also called magic methods
        self.put(key, value)

    def __getitem__(self, key):
        #another common dunder (double underscore) method
        return self.get(key)

#make hashtable ht and give it a size
ht = HashTable(50)

#add some items
ht["AZ"] = "Biden"
ht["OK"] = "Trump"
ht["PA"] = "Biden"
ht["NM"] = "Biden"
ht["TX"] = "Trump"


print ()

name = "Joe"
age = 27



#match keys to values - note there is no key "GA" defined
for key in ("AZ","GA","NM","OK","PA","TX"):
    value = ht[key]
    #and print them out
    if value is not None:
        print(key + ": " + value)
    else:
        print(key + ": None")

print ()

#count the actual values in ht, not the slots
print("The number of elements is: {}".format(ht.count))
