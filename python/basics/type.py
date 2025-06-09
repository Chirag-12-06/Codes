# Type conversion (Automatically)
a = 3
b=5.6
print(a+b)

# Type Casting (Manually)
a=4
b="5"
c=int(b)
print(a+c)

d=float(b)
print(a+d)

e="5.67"
# ERROR
# c=int(e)
# print(a+c)

d=float(e)
print(a+d)


# Strings
c="aPPLEPP"
print(c[-3:-2])
print(c.endswith("e"))

print(c.capitalize())
print(c)

print(c.replace("P","D"))
print(c.find("d"))

print(c.count("PP"))