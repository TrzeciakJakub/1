from multiprocessing.pool import TERMINATE
from tkinter.tix import INTEGER


print("")
tekst = "HangMan Game\n"
print(tekst.center(80))
tekst2 = "Wybierz Poziom Trudnosci\n"
print(tekst2.center(80))
print("1 = Latwy   \n2 = Sredni \n3 = Trudny \n")



def is_number(userInput):
    value = str(userInput)
    if value.isdecimal(): 
            return True
    else: 
        return False
    pass

ifUserAnswered = False

while ifUserAnswered == False:
    answer = input("Wybieram Poziom: ")
    if answer:
        if answer.isdecimal():
            ifUserAnswered = True
            print("Wybrales poziom: %s  ------>>> Zaczynamy!"% answer)
        else:
            print("Nieprawidlowy wybor- musisz wybrac 1/2/3")

#def ask_for_a_difficulty(force_validnput):
    #while True:
#        a = input("Wybieram Poziom: ")
#        a_difficulty = is_number(a)
#        if a_difficulty is False:
#            print("Nieprawidlowy wybor- musisz wybrac 1/2/3")
#        else:
#            print("Wybrales poziom: %s  ------>>> Zaczynamy!"%a)
#        return 

        
import random
#words = ['cat', 'dog','zebra','whale','doplhin']
#def pick_a_word():
#    word_position = random.randint(0, len(words) -1)
#    return words[word_position]

#print(pick_a_word())

words = ["dog", "cat", "elephant", "rabbit", "mouse", "horse", "hamster", "giraffe", "snake", "gepard", "duck", "antelope", "hippo", "apple", "pizza", "strawberry", "milk", "spaghetti", "mayonnaise", "juice", "chocolate", "scissors", "ball", "computer", "headphones", "microwave", "fridge", "programmer", "hairdresser", "doctor", "engineer", "restaurant", "library", "museum", "cinema", "game", "guitar", "bike", "skateboard", "piano"]
def get_word():
    word == "" 
    word = random.choice(words)
    return word.upper()


#def menu():
#    while True:
#        a = ask_for_a_difficulty(True)
        
       

#    pass
#if __name__ == '__main__':
#    menu()




# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
difficulty = "1" # sample data, normally the user should choose the difficulty


# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
lives = 5 # sample data, normally the lives should be chosen based on the difficulty


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"


# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions


# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
already_tried_letters = [] # this list will contain all the tried letters


# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".


# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.



# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4
