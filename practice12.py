def calculate_bmi(weight: float, height: float):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        return bmi
    

def bmi_status(bmi: float):
    if 0 < bmi < 18.5:
        return "Ozg'inlik"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Ortiqcha vazn"
    elif bmi >= 30:
        return "Semizlik"
    else:
        return "Noto'g'ri kiritgansiz!"
    
boy = float(input("Bo'yingizni kiriting (m):  "))
ogirlik = float(input("Og'irligingizni kiriting (kg):  "))
bmi = calculate_bmi(ogirlik,boy)
print(bmi_status(bmi))