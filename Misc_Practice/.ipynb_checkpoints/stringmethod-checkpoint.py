def upper(my_str):
    return my_str.upper()

s = "I am awesome!"

print(s)
print(upper(s))
print(s)
print(s.upper())
print(s)

s2 = "You are awesome!"

print(s.upper(), s2)
print(s, s2.upper(), sep="\t")
print(s.upper(), s2.upper(), sep=" and ")

print(s.swapcase())
print(s.title())

print(s2.replace("a", "Y"))

s_upper = s.upper()
print(s_upper)

