def ask_question(question: str, correct_answer: str):
    return correct_answer

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Siz to'g'ri topdingiz! ")
    else: 
        print("Siz noto'g'ri javob berdingiz. Qaytadan urinib ko'ring.")

question = input("Savol:  ")
correct_answer = input("To'g'ri javob:  ").lower()
user_answer = input("Sizning javobingiz:  ").lower()
togri_javob = ask_question(question,correct_answer)
print(question)
check_answer(user_answer,togri_javob)


