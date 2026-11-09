value = 1
while value == 1:
    num = float(input("Input any number here: "))

    if num <= 1:
        print("Input a value that is greater than 1! ")
    elif num > 1:
        for given_multiplier in range(1, 13):
            print(f"{num} * {given_multiplier} = {num *  given_multiplier}")
    else:
        print("Enter a valid number!")

    status = input("Enter 5 to end, or any other key.")
    if status == "5":
        value = 0
