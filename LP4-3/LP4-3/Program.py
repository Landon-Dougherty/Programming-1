eggcount = int(input("Enter # of eggs purchased: "))
price = 0 

if eggcount >= 0 and eggcount <48:
    price = 0.50
elif eggcount >=48 and eggcount <72:
    price = 0.45
elif eggcount >=72 and eggcount <132:
    price = 0.40
elif eggcount >=132:
    price = 0.35
else:
    print("Invalid Egg Count Input")

eggcost = eggcount * price
print ("Total Egg Price : $" + str(eggcost))
input()
