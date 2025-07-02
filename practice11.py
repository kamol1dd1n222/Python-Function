def calculate_tax(salary: float):
    if salary > 0:
        if salary <= 5_000_000:
            tax = (salary / 100) * 13
            return tax
        else:
            tax = (salary / 100) * 20
            return tax
    else:
        print("Maosh 0 dan kam bo'lishi mumkin emas!")
        return 0    
def calculate_net_salary(salary: float):
    tax = calculate_tax(salary)
    qolgan_maosh = salary - tax
    return qolgan_maosh
salary = float(input("Maoshingzi: "))
print(f"Siz to'lashingiz kerak bo'lgan soliq miqdori: {calculate_tax(salary): ,.2f}")
print(f"Soliqsiz maoshinhiz:  {calculate_net_salary(salary):,.2f}")