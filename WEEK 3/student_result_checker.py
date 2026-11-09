name = input("Enter the student's name: ")
course_work = float(input("Enter the Coursework score: "))
Examination_score = float(input("Enter the Examination score: "))

if not(0 <= course_work <= 30 and 0 <= Examination_score <= 70 ):
    
    print("Invalid score entered! ")
else:
    total = course_work + Examination_score
    if total >= 70:
        grade = "A"
    elif total:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 45:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"
    decision = "Pass" if total >= 50 else "Result required"
    print()
    print("STUDENT RESULT SUMMARY")
    print("======================")
    print(f"Name: {name}")
    print(f"Coursework: {course_work: .2f}/30")
    print(f"Examination: {Examination_score: .2f}/70")
    print(f"Total: {total}/100")
    print(f"Grade: {grade}")
    print(f"Decision: {decision}")
