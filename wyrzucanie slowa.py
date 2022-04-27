#DZIALAJACA WERSJA WYRZUCANIA SLOWA JAKO _ _ _ _ _ _
#import random
#print("Hello World!")
#words = ['cat', 'dog','zebra','whale','dolphin', 'giraffe', 'at']
#def pick_a_word():
#    word = random.choice(words).upper()
#    new_word = word 
#    for i in range(0, len(word)):
#        new_word = new_word.replace(word[i], ' _ ')
#    return(new_word)  
#print(pick_a_word())
###############################

import random
##############################3
#WYRZUCANIE CALEJ LINI Z PLIKU 
#print(random.choice(list(open('countries-and-capitals.txt'))))
#############################################################################
#
#Dzialajce sciaganie slow z pliku zewnetrznego - ale tylko 1 wyrazu 

import random
print("Hello World!")
def pick_a_word():
    word_file = open("countries-and-capitals.txt",'r+')
    word = random.choice(word_file.read().split())
    word_file.close()
    new_word = word 
    #for i in range(0, len(word)):
    #   new_word = new_word.replace(word[i], ' _ ')
    return(new_word)  
print(pick_a_word())




# PYTANIE CZY CHCE ZAGRAC PONOWNIE - DZIALAJACE 

#play_game = input("Would You like to play again? (Y/N)").upper()
#if play_game == "Y":
#        print(pick_a_word())
#elif play_game == "N":
#         print("Thanks You for playing")
#else:
#    print("Please select Y or N")
#print(play_game)

# Pytanie o ponowna gre 
#answer = ""
#while answer != "Y" and answer != "N":
#    answer = input("Enter 'Y' for Yes or 'N' for 'No: "  ).upper()
#    if answer == "Y":
#        print("Let's play again!")
#        print(pick_a_word())
#        answer = "Y"
#    elif answer == "N":
#        print("Thank You for playing")
#        answer = "N"
#    else:
#        print("Please select again")



    #if input("Would You like to play again? (Y/N)\n ").upper() == "Y":
    #    word = pick_a_word()
    #    print(word)
    #else:
    #    print("Thanks You for playing")


