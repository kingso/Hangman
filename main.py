import random
from words import words

def main():
    print("PLAY HANGMAN!")
    game_over = False
    current_word = random.choice(words) 
    guessed_letters = set()
    wrong_guesses = 0
    

    while not game_over:
        if wrong_guesses > 6:
            print_stand(wrong_guesses)
            print("Sorry, you've run out of guesses. The word was:", current_word)
            game_over = True
            continue
        print_stand(wrong_guesses)
        print("Guessed letters:", ", ".join(sorted(list(guessed_letters))))
        for letter in current_word:
            if letter in list(guessed_letters):
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("")
        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        
        if guess.isalpha() and len(guess) == 1:
            guessed_letters.add(guess)
            if guess in current_word:
                
                print(f"Good guess! The word contains the letter '{guess}'.")
                set_test = set(current_word) & guessed_letters
                if set(current_word) == set_test:
                    print("Congratulations! You guessed the word!")
                    game_over = True
                    break
                continue
            else:
                print(f"Sorry, the word does not contain the letter '{guess}'.")
                wrong_guesses += 1
                continue
        else:
            print("Invalid input! Please enter a single letter.")
    
    print("Game over! The word was:", current_word)

def print_stand(wrong_guesses = 0):
    top = ("___________", 
             " |    |    ")
    body = {0: " |    O ",
            
            1: " |    | ", 
            2: " |   /| ", 
            3: " |   /|\\", 

            4: " |    | ", 

            5: " |   /  ",
            6: " |   /\\ "}
    bottom = ("----------")
    for i in top:
        print(i)
    for i in range(7):
        match wrong_guesses:
            case 1:
                print(body[0])
                break
            case 2:
                print(body[0])
                print(body[1])
                break
            case 3:
                print(body[0])
                print(body[2])
                break
            case 4:
                print(body[0])
                print(body[3])
                break
            case 5:
                print(body[0])
                print(body[3])
                print(body[4])
                break
            case 6:
                print(body[0])
                print(body[3])
                print(body[4])
                print(body[5])
                break
            case 7:
                print(body[0])
                print(body[3])
                print(body[4])
                print(body[6])
                print(" | ")
                break
        
    for i in range(1, 8 - wrong_guesses):
        print(" | ")

    
    print(bottom)
        
    

if __name__ == "__main__":
    main()

