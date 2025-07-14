import random

def hangman():
    words_with_hints = [
        ('python', 'A popular programming language'),
        ('random', 'Used to select items unpredictably'),
        ('coding', 'Another word for programming'),
        ('hangman', 'The name of this game'),
        ('simple', 'Opposite of complex'),
        ('delhi','capitalof india')
    ]
    
    word, hint = random.choice(words_with_hints)
    guessed_letters = []
    attempts = 6
    used_hint = False
    word_display = ['_'] * len(word)

    print("🎯 Welcome to Hangman with Hints!")
    print("Guess the word one letter at a time.")
    print("You have 6 incorrect guesses allowed.")
    print("Type 'hint' to get a clue (only once).\n")

    while attempts > 0 and '_' in word_display:
        print("Word: ", ' '.join(word_display))
        print("Guessed letters: ", ' '.join(guessed_letters))
        guess = input("Enter a letter or type 'hint': ").lower()

        if guess == "hint":
            if not used_hint:
                print("💡 Hint:", hint + "\n")
                used_hint = True
            else:
                print("⚠️ You have already used your hint.\n")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Good guess!\n")
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! You have {attempts} attempts left.\n")

    if '_' not in word_display:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Out of attempts! The word was:", word)

# Run the game
hangman()
