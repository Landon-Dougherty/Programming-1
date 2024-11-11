lst = [1, 2, 3] # List
tpl = (1, 2, 3) # Tuple - #immutable (Can't be modified), allows unpacking
a, b, c = tpl
print(tpl)

dct1 = {1: "apples", 2: "oranges", 3: "pears"} 
dct2 = {"name": "John", "color": "red", 0: [1, 2, 3]}

print(dct1[2]) #Will print #2 in dictionary 1 
print(dct2["name"]) # Print out value for "name" in dictionary 2 
print(dct1) # Print out entire dictionary 
print(dct1.keys()) # All #'s in dictionary, excluding values to #
print(dct1.values()) # All values of #'s in dictionary

input()