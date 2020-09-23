def avg(lst):
    
    total = 0
    count = 0
    
    for i in lst: 
        total += i
        count += 1
        
    return total / count


assert avg([1]) == 1
assert avg([1,2]) == 1.5
assert avg([1,2,3,4,5,6]) == 3.5

print(avg([1]))
print(avg([1,2]))
print(avg([1,2,3,4,5,6]))