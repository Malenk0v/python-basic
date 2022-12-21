weigth = int(input("Weight: " ))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = weigth / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weigth * 0.45
    print("Weight in Kgs: " + str(converted))


