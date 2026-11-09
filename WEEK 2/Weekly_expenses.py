print("WEEKLY EXPENSE CALCULATOR")
print()

name = input("Student Name: ")
Daily_transport_cost = float(input("Daily transprt cost: "))
Daily_feeding_cost = float(input("Daily feeeding cost: "))
number_of_days_on_campus = float(input("Days on campus: "))
print()
Other_weekly_expenses = float(input("Other Weekly expenses: "))

Transport_total = Daily_transport_cost * number_of_days_on_campus 
Feeding_total = Daily_feeding_cost * number_of_days_on_campus 
Weekly_total = Transport_total + Feeding_total + Other_weekly_expenses


print()
print("WEEKLY EXPENSE CALCULATOR")
print(f"Student: {name}")
print(f"Transport total: NGN{Transport_total: .2f}") 
print(f"Feeding Total: NGN{Feeding_total:.2f}")
print(f"Other expenses: NGN{Other_weekly_expenses: .2f}")
print(f"Weekly Total: NGN{Weekly_total: .2f}")

      

