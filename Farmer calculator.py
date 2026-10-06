# Field harvest
field1 = 100
field2 = 250
field3 = 50
field4 = 150
field5 = 150
#Calc total and average
total = field1+field3+field2+field4+field5
average = total / 5
print(" Total Harvest   :", total, "kg")
print("Average of total crop   :", average, "kg")

# Price per kg is $10
price_per_kg = 10
earnings = total * price_per_kg
print("Total earing   : $", earnings)
print()
# Packing crops into bags of 50 kg
bags  = total // 50
leftover = total % 50
print("Full bags packed  : ", bags)
print(" Leftover grain  : ", leftover, "kg")
# Comparing last year harvest
last_year = 620
print("Better than last year?   : ", total > last_year)
print(" Same as last year?   : ", total == last_year)
print()
# Bonus of 50
total += 50
print("After bonus crop   : ", total, "kg")
# Saving 25 kg for next year as seeds
total -= 25
print(" After saving   : ", total, "kg")
# Final count of bags
bags = total // 50
print("Final bag count  :", bags)
leftover = total % 50
print(" Left overs after extras and savig : " ,leftover)