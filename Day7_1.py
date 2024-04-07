age = int(input("Enter age : "))

if age < 18:
    print("Driving Condition: permission denied")
else:
    loc = input("Where do u want to go?")
    if loc == "Lashio" or loc == "Kachin":
        print("Permission deined :",loc)
    else:
        print("Permission accept :",loc)