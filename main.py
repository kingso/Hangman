import string
from words import words
import random

alphabet = set(string.ascii_uppercase)
letters = {''}
picked = ''
goes = 0


def pick_word():
    rnd = random.randint(1, len(words))
    pick = words[rnd]
    return pick


picked = pick_word()
guessed = ['_'] * (len(picked))

print('Welcome to Hangman!')
print(f'Your word is {len(picked)} letters long, good luck!')

while '_' in guessed:
    goes += 1
    print(''.join(guessed))
    print('')
    letter = input('Please type a letter: ').upper()

    if letter in letters:
        print('You\'ve already tried that letter!')

    if (letter in picked) and (letter not in letters):
        print('Well done, that letter is in the word!')
        for i, a in enumerate(picked):
            if a == letter:
                guessed[i] = letter

    letters.add(letter)
    print('Letters: ', ''.join(sorted(letters)))

print(
    f'Well done, you\'ve guessed the word {picked} correctly, it took you {goes} goes!'
)
