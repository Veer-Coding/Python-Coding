agent_v = 5
if type(agent_v) is int:
    print("Agent V is an integer")
else:
    print("Agent V is not a integer")
agent_s = 7.0
if type(agent_s) is not float:
    print("Agent S is not a Float")
else:
    print("Agent S is a Float")
#Spys
spy_s = 345
spy_v = 345
if spy_s is spy_v:
    print("Spy V and Spy S are the same identity")
spy_s = 347689
if spy_v is not spy_s:
    print("Different Identity")