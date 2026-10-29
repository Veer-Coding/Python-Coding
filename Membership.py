print("Enter score of:")
maths = int(input("Maths : "))
eng = int(input("English : "))
hass = int(input("HaSS : "))
science = int(input("Science : "))
tot = maths + eng + hass + science
avg = int(tot / 4 )
#Ranks
if avg not in range(0, 101):
    print("Ïnvalid")
elif avg in range(0,35):
    print("You are a survivor")
elif avg in range(36,75):
    print("You are a expert")
else:
    print(" You are a Elite")