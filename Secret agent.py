# making inputs
name = input(" Enter your code name you want to be called, Agent:")
gadget = input("Enter yor favourite gadget as a spy :")
# Dummy values for the agent
agent_number = 7
speed_rating = 5.98
mission_count = 56
height_m = 1.97
is_active = True
print("\n*********************************\n")
# Agent details
print("Name:", name, "-> type:", type(name))
print("Fav Gadget:", gadget, "-> type:", type(gadget))
print("agent number:", agent_number, "-> type:", type(agent_number))
print("Speed Rating:", speed_rating, "-> type:", type(speed_rating))
print("Mission Count:",mission_count, "-> type:", type(mission_count))
print("Height in meters:", height_m, "-> type:", type(height_m))
print("Is active:", is_active, "-> type:", type(is_active))
print("\n************************************\n")
# String values
agent_number_text = str(agent_number)
mission_count_text = str(mission_count)
speed_rating_text = str(speed_rating)
status_text = str(is_active)
print("Agent Number as a text:", agent_number_text, "->type:", type(agent_number_text))
print("Mission count as a text:", mission_count_text, "->type:", type(mission_count_text))
print("Speed as a text:", speed_rating_text, "->type:", type(speed_rating_text))
print("Status as a text:", status_text, "->type:", type(status_text))
# Slice the name
first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter
print("First three letters of name: ", first_three)
print("Last letter of the name:", last_letter)
print("Your code name is : ", code_name)
# Reverse the string 
reversed_gadget = gadget[ : :-1]
print(" Reversed gadget name : ", reversed_gadget)
# Creating badge lines
badge_line_1 = "AGENT " + code_name.upper()
badge_line_2 = "ID: " + agent_number_text + " | MISSIONS: " + mission_count_text
badge_line_3 = "SPEED: " + speed_rating_text + " | ACTIVE: " + status_text
badge_line_4 = " SECRET GADGET CODE: " + reversed_gadget.upper()
# Print badge lines
print(" ")
print("******** SECRET AGENT BADGE ***********")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("******************************************")