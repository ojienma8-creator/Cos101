number = int(input("Enter a number: "))
s_multiplier = int(input("Enter a starting multiplier: "))
e_multiplier = int(input("Enter an ending multilier: "))
print()


for multiplier in range(s_multiplier, e_multiplier):
    result = number * multiplier
    if s_multiplier <= e_multiplier:
        print(f"{multiplier} * {number} = {result}")
    else:
        print("Error: Starting multiplier cannot be greater than Ending Multiplier!")
    
