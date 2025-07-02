def get_grade(score:int):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 60 <= score <= 79:
        return "C"
    elif 0 <= score <= 59:
        return "F"
    else:
        return "Siz mavjud bo'lmagan ballni kiritdingiz! "
score = int(input("Your score:  "))
print(get_grade(score))