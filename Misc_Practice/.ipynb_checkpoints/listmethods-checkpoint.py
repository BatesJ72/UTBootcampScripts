l = [9,1,2,4,5,7,3]
print(l)
l.reverse()
print(l)
l.sort()
print(l)

# common mistake
k = l.sort()
print(k)
# List methods don't return anything, so "nothing" is stored in the new variable. List methods only modify the original, they don't return anything.  

