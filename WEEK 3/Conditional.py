score = float(input("Enter your score: "))
if (0 <= score <= 100):
    if (0<= score < 50):
        print("You failed!")
    elif (50 <= score < 70):
        print("You passed")
    elif score >= 70:
        print("You are a Distinction Student! ")
    elif score >= 90:
        print("You are exceptional!")
else:
    print("invalid score")


      
        
