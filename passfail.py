student_score = {
    'Nevin': 90,
    'Bobby': 20,
    'Bruce': 80,
}

pass_fail = {}

for student in student_score:
    score = student_score[student]
    if score > 89:
        pass_fail[student] = 'Great!'
    elif score > 79:
        pass_fail[student] = 'Okay'
    else:
        pass_fail[student] = 'Fail'

print(pass_fail[student])