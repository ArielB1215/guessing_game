import random

def is_higher(guess, secret):
    if(guess > secret):
        return True

def is_lower(guess, secret):
    if(guess < secret):
        return True

def is_correct(guess, secret):
    if(guess == secret):
        return True

def main():
    secret_num_to_guess = random.randint(1, 100)
    guessed_num = int(input("Hello! Enter a number between 1 - 100: "))
    while True:
        if is_lower(guessed_num, secret_num_to_guess):
            print("Your guess is lower than the secret number")
            guessed_num = int(input("Hello! Enter a number between 1 - 100: "))
        if is_higher(guessed_num, secret_num_to_guess):
            print("Your guess is higher than the secret number")
            guessed_num = int(input("Hello! Enter a number between 1 - 100: "))
        if is_correct(guessed_num, secret_num_to_guess):
            print("Your guess is correct! Good job:)")
            break


if __name__ == '__main__':
    main()