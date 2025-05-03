import random

def choose_word():
    with open("hangman_words.txt") as f:
        words = [line.strip() for line in f]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def main():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman... to lose!!")

    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("How many times will you repeat the same thing?")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("OoOoOo not bad, it was a good guess.")
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts left.\nGet good.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nMeh! Pure Luck. You guessed the word \"{word}\" somehow.")
            return

    print(f"\nLoser! Ha Ha Ha!! \nYou couldn't even guess the word \"{word}\"")


if __name__ == "__main__":
    main()