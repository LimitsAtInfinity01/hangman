import random
def main():
    words = [
    # Simple words
    "apple", "banana", "cherry", "grape", "orange",
    "table", "chair", "window", "pencil", "paper",
    "school", "garden", "bridge", "mountain", "river",
    "family", "friend", "summer", "winter", "autumn",
    "music", "movie", "planet", "ocean", "desert",
    "flower", "animal", "cloud", "mirror", "travel",

    # More complex words
    "mystery", "ancient", "whisper", "journey", "invisible",
    "adventure", "memorable", "crescent", "treasure", "phantom",
    "benevolent", "solitude", "lighthouse", "astronomy", "wilderness",
    "paradise", "horizon", "sanctuary", "labyrinth", "serenity",
    "ephemeral", "kaleidoscope", "perseverance", "phenomenon", "quarantine",
    "renaissance", "allegiance", "catastrophe", "magnificent", "endeavor",
    "symmetry", "vocabulary", "universe", "metaphor", "silhouette"
]

    winner = False
    dict_word = {}
    blank_word = []
    random_word = random.choice(words)

    for letter in random_word:
        blank_word.append('_')

    for letter in blank_word:
        print(letter, end='')
    print()
    print(len(blank_word))
    print(hangmanart()[0])

    strike = 0
    points = 0
    while(winner == False):
        guess = input("Enter your guess, one letter at a time: ")
        for i in range(len(random_word)):
            if guess not in random_word:
                strike += 1
                print(hangmanart()[strike])
                break
            elif guess == random_word[i]:
                blank_word[i] = guess
                points += 1

        for letter in blank_word:
            print(letter, end='')
        print()  
        print('Strikes: ', strike)
        print('Points: ', points)

        if strike == 5:
            print("Strikes", strike)
            print("The Pirate is dead!")
            break
        elif points == len(blank_word):
            winner = True
            print("You won")

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