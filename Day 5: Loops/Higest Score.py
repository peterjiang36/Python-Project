student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]

total_exam_score = sum(student_scores)
print(total_exam_score)

score_sum = 0
for score in student_scores:
    score_sum += score
print(score_sum)

print(max(student_scores))

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

sum = 0
for number in range(1, 101):
    sum += number
print(sum)