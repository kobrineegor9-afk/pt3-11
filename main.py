import random

def show_history(attempts_history):
    print('/n history:')
    for i, (guess, result) in enumerate(attempts_history, 1):
        print(f'{i}, {guess} -> {result}')

def main():
    print('добро пожалаловать в игру кгадай число!')
    print('я загадал число от 1 до 100,попробуй угадать!')

    secret_number = random.randint(1,100)
    attempts = 0
    attempts_history = []

    while True:
        guess = input('your opinion').lower()
        attempts += 1

        if not guess.isdigit():
            print("пожалуйсто введите число!")
            continue

        guess = int(guess)

        if guess < secret_number:
            print('загадочное число больше!')
        elif guess > secret_number:
            print('загаданное число меньше')
        else:
            print(f'ура ты угадал за {attempts} попыток')

if __name__ == '__main__':
    main()

