def age_calculator(birth_year,now_year):
    age = now_year - birth_year
    print(age)
    if age > 18:
        print("Siz balog'atga yetkansiz!")
    else:
        print("Siz balog'atga yetmagansiz!")
now_year = 2025
birth_year = int(input("Birth year:  "))
age_calculator(birth_year,now_year)