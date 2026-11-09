print("Title; Student's Weekly Expense Calculator; ")
print()

name = input("Enter your name: ")
Daily_transport_cost = float(input("Enter your daily transprt cost: "))
Daily_feeding_cost = float(input("Enter your Daily feeeding cost: "))
number_of_days_on_campus = float(input("Enter your number of days on campus: "))
Other_weekly_expenses = float(input("Enter your other expenses for the week: "))

Transport_total = Daily_transport_cost * number_of_days_on_campus 
Feeding_total = Daily_feeding_cost * number_of_days_on_campus 
Weekly_total = Transport_total + Feeding_total + Other_weekly_expenses


print()
print(f"Hello, {name}")
print(f"Your Total Transport cost is: {Transport_total: .2f}") 
print(f"Your Total Feeding is: {Feeding_total: .2f}")
print(f"Your Total Weekly cost is: {Weekly_total: .2f}")
      
