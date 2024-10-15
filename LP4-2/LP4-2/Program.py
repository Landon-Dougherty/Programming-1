print "Hello, World!"
weight = int(input("Enter Weight In Kilos: "))
length = int(input("Enter Length In Centimeter: "))
width  = int(input("Enter Width In Centimeter: "))
height = int(input("Enter Height In Centimeter: "))

CubMet = length * width * height

if weight <=27 and CubMet <= 100000:
    print("Package Is Good")
elif weight >27 and CubMet <=100000:
    print("Package Is Too Heavy")
elif weight <=27 and CubMet >100000:
    print("Package Is Too Large")
elif weight >27 and CubMet >100000:
    print("Package Is Too Heavy And Too Large")
else:
    print("Invalid Package Logistics")
    


input()