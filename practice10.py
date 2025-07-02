def is_strong_password(password: str):
    if password.isalnum()  and len(password) > 8: #isalnum() ishlatdim chunki parolda raqam ham qatnashishi kerak va bu masala shartiga ta'sir qilmaydi
        return "Kuchli parol"
    else: 
        return "Parol kuchli emas! Kuchliroq parol yarating!!!!"
password = str(input("Your password:  "))
print(is_strong_password(password))