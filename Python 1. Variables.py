x = 22

print(x)

type(x)

y = ("Mint Chocolate Chip")
print(y)

print(type(y))

# Variables are case sensitive

x, y, z = "chocolate", "vanilla", "rocky road"
print(x)
print(y)
print(z)

ice_cream = ["chocolate", "vanilla", "rocky road"]
x, y, z, = ice_cream
print(x)
print(y)
print(z)

# Best practices for naming variables
# Camel Case e.g. testVariableCase
# Pascal case e.g. TestVariableCase
# Snake Case e.g. test_variable_case - improves readability

test_var = "vanilla swirl"
print(test_var)

# for a variable, must stick to same type (e.g. string, integers)
x = "ice cream"
y = 2
#print(x+y) # does not work
print(x,y) # does work