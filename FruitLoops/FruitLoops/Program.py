﻿colors = ["red", "green", "blue"] 
print(colors)
print(colors[1]) # Green 

fruits = ["apple", "banana" , "orange" , "kiwi", "mango"]
# For-each loop 
for item in fruits: 
    print(item)
print("")
# For loop
for index in range (len(fruits)): # Range in 0 to Fruits
    print(fruits[index])
print("")

# lastfruit = fruit[len(fruits)-1] 
lastfruit = fruits[-1]
print(lastfruit)

input()