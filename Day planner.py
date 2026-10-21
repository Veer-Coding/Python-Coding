#school day planner
print(" ************* School day planner ************")
print(" Answer 3 questions and I will plan your day")
day   = input(" What day is it{Monday to Sunday}").strip().capitalize()
weather   = input(" What is the waether like? { sunny / cludy / rainy}").strip().lower()
homework = input(" Is your homework done? { Yes or No}").strip().lower()
print()
print(f"=== Your planner for {day} ===") 
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# if elif else
if day in ("Saturday", "Sunday"):
    print("Day type  : Weekend - enjoy your life. you might want to do some of your hobbies")
elif day == "Monday":
    print(" Day type: First day back to waking up it may be boring but do not give up")
elif day == "Friday":
    print(" Day type: Last day of weekdays woohooo!  Watch a movie with your family at night if you want to")
elif day in  ("Tuesday", "Wednesday", "Friday"):
    print(" Do not worry it will be over soon but focus in class")
else:
    print(" Day has not been entered correctly { Check spelling}")
    # Weather with AND operator
if weather == "sunny" and homework == "yes":
    print(" Go outside and play sports and relax")
    # OR operator
if weather == "rainy" or weather == "cloudy":
    print(" Take an umbrella")
# NOT  operator
if not (homework == "yes"):
    print(" Homework  : Not done yet. Finish it before anything")
#AND + OR + IF
if weather == "rainy" and not (homework == "yes"):
    print(" The best thing to do is finish the homework and relax")
elif weather == "sunny" and homework == "yes" and not (day in("Saturday", "Friday")):
    print(" You are ready for school so relax")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print(" Go outside with family or frieds")
elif day in ("Sunday") and homework == "yes":
    print(" Sunday nights are always sad but you are prepared")
else:
    print(" Take it step by step, you will get there ")

    print()
print(" Plan complete! ")