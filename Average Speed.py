a = int(input("Enter value"))
b = int(input("Enter value 2"))
c = int(input("Enter value 3"))
avg = (a + b + c) / 3
if avg > a and avg < b:
    print("%d is faster than %d" % (b, a))
elif avg < a and avg > b and avg > c:
    ("Cyclist A is the fastest")
elif avg < b and avg > a and avg > c:
    ("Cyclist B is the fastest")
elif avg < c and avg > b and avg > a:
    ("Cyclist C is the fastest")
elif avg > 120:
    print("Cyclists going to fast. Wave the signal")
elif avg < a and avg < b and avg < c:
    print("Cyclists are going too slow. Cheer Them")
else:
    print("Invalid input")
