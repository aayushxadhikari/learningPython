
# num2 = num1

# print("Before num1 value is updated:")

# print("num1: ", num1)
# print("num2: ",num2)


# print("\n num1 points to: ",id(num2))
# print("num2 points to: ",id(num2))

# num2 = 22

# print("\nAfter num2 value is updated:")

# print("num1: ", num1)
# print("num2: ",num2)


# print("\n num1 points to: ",id(num2))
# print("num2 points to: ",id(num2))


dict1 = {
    'value':11
}
dict2 = dict1

print("dict1: ", dict1)
print("dict2: ",dict2)

print("\n num1 points to: ",id(dict1))
print("num2 points to: ",id(dict2))

dict2['value'] = 22

print("\n After the value is updated:")

print("dict1: ", dict1)
print("dict2: ",dict2)

print("\n num1 points to: ",id(dict1))
print("num2 points to: ",id(dict2))



