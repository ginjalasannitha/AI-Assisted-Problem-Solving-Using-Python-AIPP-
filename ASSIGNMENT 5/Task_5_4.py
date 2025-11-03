def score_applicant(name, experience, age):
    score = experience * 10
    if 22 <= age <= 35:
        score += 5
    return score

print("John's score:", score_applicant("John", 3, 24))
print("Mary's score:", score_applicant("Mary", 3, 24))
