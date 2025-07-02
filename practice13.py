def is_palindrome(text: str):
    if text.isalpha():
        text = text.lower()
        revorse_text = text[::-1]
        return text == revorse_text
    else:
        return "Faqat Hrflardan iborat bo'lishi kerak!"
    
text = input("Text:  ")
print(is_palindrome(text))