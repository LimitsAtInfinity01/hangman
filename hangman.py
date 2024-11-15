import random
def main():
    words = ['papa', 'mama', 'speaker']
    winner = False
    dict_word = {}
    blank_word = []
    random_word = random.choice(words)
    for letter in random_word:
        blank_word.append('_')

    for letter in blank_word:
        print(letter, end='')
    print(hangmanart()[0])

    strike = 0
    while(winner == False):
        guess = input("Enter your guess, one letter at a time: ")
        for i in range(len(random_word)):
            if guess not in random_word:
                strike += 1
                print(hangmanart()[strike])
                break
            elif guess == random_word[i]:
                blank_word[i] = guess

        for letter in blank_word:
            print(letter, end='')
        print()  
        print('Strikes', strike)

        if strike == 5:
            print("Strikes", strike)
            print("The Pirate is dead!")
            break


def hangmanart():
    hangmanart = ['''
        +---+
        |   |
            |
            |
            |
        =======''','''
        +---+
        |   |
        O   |
        |   |
            |
        =======''','''
        +---+
        |   |
        O   |
       /|   |
            |
        =======''','''
        +---+
        |   |
        O   |
       /|\\  |
            |
        =======''','''
        +---+
        |   |
        O   |
       /|\\  |
       /    |
        =======''','''
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
        ======='''
        ]
    return hangmanart

if __name__ == '__main__':
    main()