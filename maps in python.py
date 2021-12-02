tel = {'jack': 4098, 'sape': 4139}   #sets up map


tel['guido'] = 4127   # adds entry to map
print tel

print tel['jack']     #extracts value associated with key

del tel['sape']       #deletes value from map


tel['irv'] = 4127      #adds entry to map
print tel

print tel.keys()       # shows keys used in map

print 'guido' in tel      # shows membership in map
