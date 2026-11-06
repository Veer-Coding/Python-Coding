coding = 1   # 001
school = 2   #010
Youtube = 3  #100

#Approved apps
approved = [
    "coding"
    "school portal"
    "Youtube"
]
#Getting details
name = input("Enter your name:")
app = input("Enter app:")
print("Identity operator")

#using is
if type(name) is str:
    print("Your name has been entered as a text")
#using is not
if type(app) is not str:
    print("The app name has been entered in a seceret code")
else:
    print("App has been entered as a number")
#Checking app
if app in approved:
    print("You can enter to this app")
else:
    print("App cannot be accessed. Check settings")