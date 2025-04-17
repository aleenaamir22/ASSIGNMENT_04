import random

# Word bank list
words_list = ['pulchritudinous', 'travel', 'extend', 'result', 'nausea', 'accommodation']

# Choosing random word from word list
word = random.choice(words_list).lower()

guessed_letters = []#empty list
attempts = 7#total number of attempts
#prints
print("Hangman Game")
print("Guess the word:")
print(" ".join("_" for _ in word))

while attempts > 0:
    user_input = input("\nEnter a letter: ").lower()#user input

    if len(user_input) != 1 or not user_input.isalpha():
        print("🚫 Please enter a single letter (a-z).")
        continue

    if user_input in guessed_letters:
        print("⚠️ You've already guessed that letter. Try a new one.")
        continue

    guessed_letters.append(user_input)

    if user_input in word:
        print("✅ Correct guess!")#if the word is right
    else:
        attempts -= 1
        print(f"❌ Wrong guess! You have {attempts} attempt{'s' if attempts != 1 else ''} left.")#if word guessed is wrong

    displayed_word = " ".join(letter if letter in guessed_letters else "_" for letter in word)#word guessed joined
    print(displayed_word)#printing

    if "_" not in displayed_word:
        print(f"\n🎉 Congratulations! You guessed the word: '{word}'")#if correct win
        break
else:
    print(f"\n Out of attempts! The correct word was: '{word}'")#if loose
