import random
import os 


def main():
    play()
 


def hangman_display(user_health):

    if user_health == 6:
         print(     "  _____ \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n")
   
    if user_health == 5:
         print(     "  _____ \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n")

    
    if user_health == 4:
         print(     "   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n")
 
    if user_health == 3:
        print(     "   _____ \n"
                   "  |     | \n"
                   "  |     |\n"
                   "  |     | \n"
                   "  |      \n"
                   "  |      \n"
                   "  |      \n"
                   "__|__\n")
    if user_health == 2:
        print(      "   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |     | \n"
                    "  |     O \n"
                    "  |      \n"
                    "  |      \n"
                    "__|__\n")
    if user_health == 1:
        print(      "   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |     | \n"
                    "  |     O \n"
                    "  |    /|\ \n"
                    "  |        \n"
                    "__|__\n")

    if user_health == 0:
     print(         "   _____ \n"
                    "  |     | \n"
                    "  |     |\n"
                    "  |     | \n"
                    "  |     O \n"
                    "  |    /|\ \n"
                    "  |    / \ \n"
                    "__|__\n")


def pick_a_random_word():
    word_file = open("words.txt",'r+')
    word = random.choice(word_file.read().split()).upper()
    word_file.close()
    return word


def play():
    nickname = input("Please enter Your Nickname: ")
    tekst = "\nHello " + nickname + ", Let's start HangMan Game!\n"    
    print(tekst.center(80))

    user_health = 6
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    used_letter = []
    new_word = pick_a_random_word()
    hidden_word = []
    for i in new_word:
        hidden_word.append("_")
    print(new_word)  #sprawdzam tylko jaki mamy wyraz zeby byl nie zasloniety

    while hidden_word != list(new_word) and user_health > 0:
        print("Your health: " + str(user_health))
        show_hidden_word(hidden_word)
        user_input = input("Please provide a letter: ").upper()
        if user_input in alphabet:
            if user_input not in used_letter:
                used_letter.append(user_input)

                if user_input in new_word:
                    print("CONGRATS! - The letter " + str(user_input)  + " is in the word")
                    count = 0
                    for i in new_word:
                        if i == user_input:
                            hidden_word[count] = str(i)

                        count += 1

                
                else:
                    print("This letter is not in the word - -1 LIFE")
                    user_health = user_health - 1  
                    hangman_display(user_health)  #(trzeba było usunąć zbędnego printa(wystarczy wywołać funkcje), bo wyświetlało się "None" bo błędnie wpisanej literce po wyświetleniu wisielca) 
                    print(used_letter)
            else:
                print("You have already used that letter!")
                
        else:
            print("Invalid character - -1 LIFE")
            user_health = user_health - 1
            print(hangman_display(user_health))
            show_hidden_word(hidden_word)     
       

    if hidden_word == list(new_word):
        print("CONGRATS! You have guessed the word correctly!")
    else:
        print("GAME OVER :( - Better luck next time!")

    play_again()    

#wyświetla podkreślniki bez cudzysłowów 
def show_hidden_word(hidden_word):
    print(' '.join(str(x) for x in hidden_word))


def play_again():
    answer = ""
    while answer != "Y" and answer != "N":
        answer = input("Do you want to play again?\nEnter 'Y' for Yes or 'N' for 'No: "  ).upper()
        if answer == "Y":
            print("Let's play again!")
            answer = "Y"
            play()
        elif answer == "N":
            print("Thank You for playing")
            answer = "N"
        else:
            print("Please select again")


if __name__ == "__main__":
    main() 