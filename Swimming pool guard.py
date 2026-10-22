print(" Hello welcome to our pool!")
print(" We are open everyday 9 AM to 8 PM")
time = input(" What is the rounded time (AM and PM)").strip().upper()
age = float(input("What is your age?"))
weather = input("What weather is it {Sunny,Rainy or Cloudy}").strip().capitalize()

# if elif else
if weather == "Sunny":
    print("What a pleasent day to swim")

elif weather == "Rainy" or "Cloudy":
    print("Don't worry our pools are shaded ")
elif age <= 8:
    print("Young swimmer, enjoy the kids pool!")

elif age <= 200:
    print("You can swim wherever you want")
elif age <= 30:
    print("Great day to hangout with friends and family")
elif time <= "8PM":
    print("You are allowed in!")
elif time in ("9PM", "10PM", "11PM", "12AM", "1AM", "2AM", "3AM", "4AM", "5AM", "6AM", "7AM", "8AM"):
    print("Pool closed come back at 9AM")
else:
    print("Something was entered wrong. Check again")