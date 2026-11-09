#total = 0

#for number in range(1, 4):
    #total = 0
    #total += number
#print("Total:", total)

n = int(input("Enter an end number (n): "))
if n < 1:
    print("Invalid input: n cannot be less than 1")
else:
    total = 0
    for number in range(1, n + 1):
        total = total + number
    print(f"The sum of 1 to {n} = {total}")
