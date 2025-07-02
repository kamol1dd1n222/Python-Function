def is_valid_phone_number(phone: str):
    return len(phone) == 9
phone = input("Phone number(991234567):  ")
print(is_valid_phone_number(phone))