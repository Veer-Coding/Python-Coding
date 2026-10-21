homework = input("  Do you have homework? Yes or no?")
# Homework
if homework == "Yes":
    print(" Do your homework first to not get in trouble")
else:
    homework = "No "

#Tests
tests = input("Any test coming up? Yes or no?")
if tests == "yes":
    print( "Study  for the test so you get good marks")

else:
    print(" That is nice")
    tests = "No"
# Tuitions or meetings
meeting = input(" Do you have any meetings or tuitions")

if meeting == "yes":
    print(" Do not forget to attend them")

else:
    print(" Alright be on time!")
    meeting = "no"

# Final check
print("*******************FINAL PLAN****************************")
print("Any meetings or tuition : ",meeting)
print("Any homework left : ",homework)
print("Any tests coming up : ", tests)
print(" If you are free you can spend time on your hobbies or do whatever you like and if you have something undone finish that first")