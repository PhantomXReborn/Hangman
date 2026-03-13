import random

HANGMAN_STAGES = [
    """
   +---+
   |   |
       |
       |
       |
       |
=========
""",
    """
   +---+
   |   |
   O   |
       |
       |
       |
=========
""",
    """
   +---+
   |   |
   O   |
   |   |
       |
       |
=========
""",
    """
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
""",
    """
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========
""",
    """
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========
""",
    """
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========
"""
]

def get_word_list():
    """Returns a list of words for the game"""
    # You can expand this list or load from a file
    return [
        "python", "programming", "computer", "algorithm", "database",
        "network", "software", "hardware", "keyboard", "monitor",
        "javascript", "html", "css", "developer", "function"
    ]

def display_game_state(word, guessed_letters, wrong_guesses):
    """Displays the current game state"""
    # Display hangman
    print(HANGMAN_STAGES[len(wrong_guesses)])
    
    # Display word with blanks
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord: " + display_word)
    
    # Display wrong guesses
    if wrong_guesses:
        print("\nWrong guesses: " + ", ".join(wrong_guesses))
    
    # Display remaining attempts
    remaining = len(HANGMAN_STAGES) - 1 - len(wrong_guesses)
    print(f"\nRemaining attempts: {remaining}")

def play_hangman():
    """Main game function"""
    # Get random word
    words = get_word_list()
    secret_word = random.choice(words).upper()
    
    # Game state
    guessed_letters = set()
    wrong_guesses = []
    
    print("=" * 50)
    print("Welcome to Hangman!")
    print("=" * 50)
    
    while len(wrong_guesses) < len(HANGMAN_STAGES) - 1:
        # Display current state
        display_game_state(secret_word, guessed_letters, wrong_guesses)
        
        # Check if word is completely guessed
        if all(letter in guessed_letters for letter in secret_word):
            print("\n🎉 Congratulations! You won!")
            print(f"The word was: {secret_word}")
            break
        
        # Get player's guess
        while True:
            guess = input("\nGuess a letter: ").upper().strip()
            
            if len(guess) != 1:
                print("Please enter a single letter.")
            elif not guess.isalpha():
                print("Please enter a letter (A-Z).")
            elif guess in guessed_letters or guess in wrong_guesses:
                print("You already guessed that letter. Try again.")
            else:
                break
        
        # Check if guess is correct
        if guess in secret_word:
            print(f"✅ Good guess! '{guess}' is in the word.")
            guessed_letters.add(guess)
        else:
            print(f"❌ Sorry, '{guess}' is not in the word.")
            wrong_guesses.append(guess)
    
    # Game over - check if player lost
    if len(wrong_guesses) >= len(HANGMAN_STAGES) - 1:
        display_game_state(secret_word, guessed_letters, wrong_guesses)
        print("\n💀 Game Over! You ran out of attempts.")
        print(f"The word was: {secret_word}")
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
    if play_again.startswith('y'):
        play_hangman()
    else:
        print("Thanks for playing! Goodbye!")

# Alternative version that reads words from a file
def play_hangman_with_file(filename="words.txt"):
    """Play hangman with words loaded from a file"""
    try:
        with open(filename, 'r') as file:
            words = [word.strip().upper() for word in file.readlines() if word.strip()]
        
        if not words:
            print("No words found in the file. Using default word list.")
            play_hangman()
        else:
            secret_word = random.choice(words)
            play_game_with_word(secret_word)
            
    except FileNotFoundError:
        print(f"File '{filename}' not found. Using default word list.")
        play_hangman()

def play_game_with_word(secret_word):
    """Play a game with a specific word"""
    guessed_letters = set()
    wrong_guesses = []
    
    print("=" * 50)
    print("Welcome to Hangman!")
    print("=" * 50)
    
    while len(wrong_guesses) < len(HANGMAN_STAGES) - 1:
        display_game_state(secret_word, guessed_letters, wrong_guesses)
        
        if all(letter in guessed_letters for letter in secret_word):
            print("\n🎉 Congratulations! You won!")
            print(f"The word was: {secret_word}")
            break
        
        while True:
            guess = input("\nGuess a letter: ").upper().strip()
            
            if len(guess) != 1:
                print("Please enter a single letter.")
            elif not guess.isalpha():
                print("Please enter a letter (A-Z).")
            elif guess in guessed_letters or guess in wrong_guesses:
                print("You already guessed that letter. Try again.")
            else:
                break
        
        if guess in secret_word:
            print(f"✅ Good guess! '{guess}' is in the word.")
            guessed_letters.add(guess)
        else:
            print(f"❌ Sorry, '{guess}' is not in the word.")
            wrong_guesses.append(guess)
    
    if len(wrong_guesses) >= len(HANGMAN_STAGES) - 1:
        display_game_state(secret_word, guessed_letters, wrong_guesses)
        print("\n💀 Game Over! You ran out of attempts.")
        print(f"The word was: {secret_word}")
    
    play_again = input("\nWould you like to play again? (y/n): ").lower().strip()
    if play_again.startswith('y'):
        play_hangman_with_file()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    # Ask user which version to play
    print("Hangman Game")
    print("1. Play with built-in words")
    print("2. Play with words from file (words.txt)")
    
    choice = input("Choose (1 or 2): ").strip()
    
    if choice == "2":
        play_hangman_with_file()
    else:
        play_hangman()