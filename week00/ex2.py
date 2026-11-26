# Whole number + decimal -> float
# String + number-> Error
# String * MUltiplication -> String repeated n times
# Convert string to number + Whole number -> float
# Value Error when converting string to number uisng int() or float()

a=int('3')
print(7+2.0)
print(int(float("3") + 5))
print("3" * 5)
print(float("3") + 5)
print(int('4') + 5)
print(a)
print(7/2) #Division operater 
print(7//2) #Floor division operator - gives the whole number part of the division

# '+' in case of string concatenates the strings. In case of numbers it adds the numbers.
b='3.7'
# print(b+5) # This will give an error because we cannot add string and number -- TypeError: can only concatenate str (not "int") to str
c=float(b)
print(b)
print(int(c))
print(c+5)