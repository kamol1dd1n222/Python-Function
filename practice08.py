def c_to_f(celsius:float):
    fahrinhiet = (celsius * 1.8) + 32
    return fahrinhiet
def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius
harorat = float(input("Harorat: "))
tanlov = int(input("1:celsius\n2:fahrinhiet   "))
if tanlov == 1:
    print(c_to_f(harorat))
elif tanlov == 2:
    print(f_to_c(harorat))
else: 
    print("Boshqa raqam kiritdingiz!")