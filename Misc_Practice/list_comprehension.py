l = [2, 5, 7, 3, 6]

# Misc. Examples

# print([e ** 2 for e in l])

# print([e ** 2 + 1 for i, e in enumerate(l)])

# print([(i, e ** 2) for i, e in enumerate(l)])


# Practical Example

data = [
    ["Ed", 31],
    ["Doug", 27],
    ["Bob", 18]
]

print(data)

# extract the first person's age
# hard to read
data[0][1]

# wouldn't this be nice?
#data[0]["age"]

# get the average age
count = len(data)

total = 0
for e in data:
    total += e[1]

avg = total / count
print(avg)


# another way to do this

# first extract the age from data
ages = [person[1] for person in data]
avg2 = sum(ages) / len(ages)
print(avg2)


# back to this: wouldn't this be nice?
#data[0]["age"]

nice_data = [{"name": row[0], "age": row[1]} for row in data]
print(nice_data)