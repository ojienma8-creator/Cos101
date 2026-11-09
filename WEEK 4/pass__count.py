pass_count = 0

for student_number in range(1, 4):
    score = float(input(f"Enter score for student: "))
    if score >= 50:
        total_score = pass_count + score
print(f"Number of passes: {total_score}")
