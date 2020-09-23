data = [1, 2, 3, 10]

count = len(data)

total = 0
for num in data:
    total += num
    
avg = total / count
print(avg)



sum1 = [num for num in data]
avg2 = sum(sum1) / len(sum1)
print(avg2)