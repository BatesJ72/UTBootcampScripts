# print all numbers in a range
# for i in range(0, 10):
#    print(i)


# print evens in the first positive 100 numbers
# for i in range(0, 100 + 1):
#    if i % 2 == 0:
#        print(i)


# print evens in the first positive 100 numbers
# for i in range(0, 101, 2):
#    print(i)
    

# l = ["a", "b", "c", "d", "e"]

# for i in range(0, len(l)):
#     print(l[i])


d = {
    "1": "3",
    "3": "4",
    "5": "6"
}

# will print just the keys
# for e in d:
#    print(e)
    

# print just the values
# for e in d:
#    print(d[e])

# print(d.values())
# print(d.keys())

# print key and value together
for k in d: 
    print((k, d[k]))
    
print(d.items())

for k, v in d.items():
    print(f"Key: {k}; Value: {v}")