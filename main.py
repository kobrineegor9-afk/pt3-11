import random
def choose_difficulty():
    print('/n choose lvl')
    print('1. easy(1-50')
    print('2. medium (1-100')
    print('3.hard (1-200')
    while True:
        choice = input('tvoi vibor(1-3):')
        if choice == '1':
            return 1,50
        elif choice == '2':
            return 1,100
        elif choice == '3':
            return 1,200
        else:
            print('chose 1,2,3')
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

