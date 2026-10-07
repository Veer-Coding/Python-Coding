friend_1 = 50
friend_2 = 65
friend_3 = 60
friend_5 = 75
friend_4 = 20
# Total and average
total = friend_1+friend_2+friend_3+friend_4+friend_5
average = total / 5
print("total number of points : ", total) 
print(" Average : ", average)
#   Prize for 30 poins
point_per_prize = 30
prizes = total // 30
leftover = total % 30
print(" Points per prize : 30")
print(" Total prizes that can be received : ", prizes)
print(" Leftover points to spend : ", leftover)
# 50 points earned
total += 10
print(" 10 Points were added to the class and the new total is :", total)
# 20  points were decreased from class
total -= 20
print(" 20 points were decreased from the class total and the new total is : ", total)
# Final number of prizes
prizes = total // 30
leftover = total % 30
print(" Final prize count for the class : ", prizes, " and the leftover points are : ",leftover)