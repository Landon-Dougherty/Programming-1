eggcount = int(input("Enter Egg Amount Here : "))
dozen = eggcount // 12.0
remain = eggcount % 12.0
remain10 = remain * 0.10
totaldozen = dozen + remain10

if totaldozen >= 0 and totaldozen < 4:
    price = 0.50
elif totaldozen >= 4 and totaldozen < 6:
    price = 0.45
elif totaldozen >= 6 and totaldozen < 11:
    price = 0.40
elif totaldozen >=11:
    price = 0.35
else: 
    print "Invalid Egg Count"
    
totalprice = float(round(12*price,2)) * totaldozen

print "Your Egg Cost : " + str(round(totalprice,2))


input()