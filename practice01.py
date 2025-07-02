def bajaruvchi(son1:int,son2:int,amal):
    if amal == '+':
        return son1 + son2
    elif amal == '-':
        return son1 - son2
    elif amal == "*":
        return son1 * son2
    elif amal == "/":
        return son1 / son2
    else:
        return "(*,/,+,-) amllardan birini kiritish kerak!"
son1 = int(input("Son1: "))
son2 = int(input("Son2:  "))
amal = input("(+,-,*,/) amallardan birini kiriting:  ")
print(bajaruvchi(son1,son2,amal))