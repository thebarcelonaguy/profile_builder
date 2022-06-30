def get_prediction(marks_10, stream_12, marks_12, stream_college, marks_college, work_exp):
    rating_score = [1, 2, 3, 5, 8]
    score_10 = 0
    score_12 = 0
    score_college = 0
    score_work_experience = 0

    marks_10 = float(marks_10)
    marks_12 = float(marks_12)
    marks_college = float(marks_college)
    work_exp = int(work_exp)

    if marks_10 <= 55:
        score_10 = 1
    elif marks_10 > 55 and marks_10 <= 60:
        score_10 = 2
    elif marks_10 > 60 and marks_10 <= 70:
        score_10 = 3
    elif marks_10 > 70 and marks_10 <= 80:
        score_10 = 5
    elif marks_10 > 80 and marks_10 <= 90:
        score_10 = 8
    else:
        score_10 = 10

    if stream_12.lower() == "science":
        if marks_12 <= 55:
            score_12 = 1
        elif marks_12 > 55 and marks_12 <= 60:
            score_12 = 2
        elif marks_12 > 60 and marks_12 <= 70:
            score_12 = 3
        elif marks_12 > 70 and marks_12 <= 80:
            score_12 = 5
        elif marks_12 > 80 and marks_12 <= 90:
            score_12 = 8
        else:
            score_12 = 10
    elif stream_12.lower() == "commerce":
        if marks_12 <= 50:
            score_12 = 1
        elif marks_12 > 50 and marks_12 <= 55:
            score_12 = 2
        elif marks_12 > 55 and marks_12 <= 65:
            score_12 = 3
        elif marks_12 > 65 and marks_12 <= 75:
            score_12 = 5
        elif marks_12 > 75 and marks_12 <= 90:
            score_12 = 8
        else:
            score_12 = 10
    else:
        if marks_12 <= 45:
            score_12 = 1
        elif marks_12 > 45 and marks_12 <= 50:
            score_12 = 2
        elif marks_12 > 50 and marks_12 <= 60:
            score_12 = 3
        elif marks_12 > 60 and marks_12 <= 70:
            score_12 = 5
        elif marks_12 > 70 and marks_12 <= 85:
            score_12 = 8
        else:
            score_12 = 10

    if stream_college.lower() == "medicine":
        if marks_college <= 55:
            score_college = 1
        elif marks_college > 55 and marks_college <= 60:
            score_college = 2
        elif marks_college > 60 and marks_college <= 62:
            score_college = 3
        elif marks_college > 62 and marks_college <= 65:
            score_college = 5
        elif marks_college > 65 and marks_college <= 70:
            score_college = 8
        else:
            score_college = 10

    elif stream_college.lower() == "ca":
        if marks_college <= 50:
            score_college = 1
        elif marks_college > 50 and marks_college <= 53:
            score_college = 2
        elif marks_college > 53 and marks_college <= 55:
            score_college = 3
        elif marks_college > 55 and marks_college <= 57:
            score_college = 5
        elif marks_college > 57 and marks_college <= 63:
            score_college = 8
        else:
            score_college = 10

    elif stream_college.lower() == "commerce":
        if marks_college <= 55:
            score_college = 1
        elif marks_college > 55 and marks_college <= 60:
            score_college = 2
        elif marks_college > 60 and marks_college <= 65:
            score_college = 3
        elif marks_college > 65 and marks_college <= 70:
            score_college = 5
        elif marks_college > 70 and marks_college <= 80:
            score_college = 8
        else:
            score_college = 10

    elif stream_college.lower() == "engineering" or stream_college.lower() == "others":
        if marks_college <= 60:
            score_college = 1
        elif marks_college > 60 and marks_college <= 65:
            score_college = 2
        elif marks_college > 65 and marks_college <= 70:
            score_college = 3
        elif marks_college > 70 and marks_college <= 75:
            score_college = 5
        elif marks_college > 75 and marks_college <= 85:
            score_college = 8
        else:
            score_college = 10

    elif stream_college.lower() == "arts":
        if marks_college <= 50:
            score_college = 1
        elif marks_college > 50 and marks_college <= 55:
            score_college = 2
        elif marks_college > 55 and marks_college <= 60:
            score_college = 3
        elif marks_college > 60 and marks_college <= 65:
            score_college = 5
        elif marks_college > 65 and marks_college <= 75:
            score_college = 8
        else:
            score_college = 10
    if work_exp < 12:
        score_work_experience = 0
    elif work_exp > 12 and work_exp <= 36:
        score_work_experience = 0.20 * (work_exp - 11)
    else:
        score_work_experience = 5

    ar_score = score_12 + score_college + score_10 + score_work_experience
    return ar_score
