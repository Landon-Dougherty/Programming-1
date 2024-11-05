thing = "HELLO world HERE is SOME text"
print(thing.lower()) #Make entire string lowercase letters
print(thing.upper()) #Make entire string uppercase letters
print(thing.capitalize()) #Capitalize First Letter
print(thing.title()) #Every First Letter of A Word Capitalized (Like This Text.)
print(thing.isdigit()) #Check is string is a valid digit, every character must be a number of some sort
print(thing.find("world")) #Also see index and rindex
print(thing.count("E")) #How many of what is in a string
print(thing[::-1]) #Reverse the string... Test --> tseT
print(thing.split(" ")) #Display each word --> ['HELLO', 'world', 'HERE', 'is', 'SOME', 'text']
print("Hello" *5) #Repeat set string X amount of times
input()