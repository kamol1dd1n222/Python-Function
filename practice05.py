from random import randomint
def check_guess(secret, guess):
    return secret == guess
def print_result(is_correct):
    if is_correct:
        print("Tog'ri topdingiz.")
    else:
        print("Topolmadingiz.")
def main():
    secret = randomint(1,9)
    