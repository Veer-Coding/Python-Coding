print("########################################")
print("             WELCOME TO RIDER         ")
print("########################################")
print(" Pick your vehicle")
print(" 1 - Bike")
print(" 2 - Aircraft")
choice = int(input(" Enter 1 or 2 : "))
if choice == 1:
    print("Pick your bike")
    print(" 1 - scooty")
    print(" 2 - Racer")
    bike_type = int(input(" Enter 1 or 2"))
    if bike_type == 1:
        print("You picked : Scooty")
        print("Top Speed : 80 km/h")
        print("Best for Streets")
    else:
       print("You picked : Racer Bike") 
       print("Top speed : 150 km/hr")
       print("Best for: Freeways and competitions")
elif choice == 2:
    print("Pick your plane type")
    print("1 - SR 71 ")
    print(" 2 - Boeing 747 (comercial)")
    aircraft_type = int(input("Pick 1 or 2: "))
    if aircraft_type == 1:
        print(" You picked : SR 71")
        print(" Top speed: Mach 3.24")
        print(" Best for: Secret bombing and pictures")
    else:
        print("You picked: Boeing 747")
        print("Top speed: 900 km/hr")
        print(" Best for: Airliners and civillian upper-deck flight")
else:
    print("***********ERORR. CHECK VALUES ENTERED**************")

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("Enjoy Your Ride")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")