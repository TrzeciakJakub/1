import random

# MENU 
print("")
tekst = "Hangman Game\n"
print(tekst.center(80))
tekst2 = "Wybierz Poziom Trudnosci\n"
print(tekst2.center(80))
print("1 = Latwy   \n2 = Sredni \n3 = Trudny \n")

#prosba o podanie poziomu trudnosci 1 2 lub 3  - ale jak wpisze litere to wywala bledy 
def is_number(a):
    #value = str(userInput)
    #if value.isdecimal(): 
    value = int(a)
    if (value >=1 and value <=3):
        return True
    elif value.isdecimal():
        return True
    else:
        return False
pass


def ask_for_a_difficulty(b):
    while True:
        a = input("Wybieram Poziom: ")
        ask_for_a_difficulty = is_number(a)
        if ask_for_a_difficulty is True:
            print("Wybrales poziom: %s  ------>>> Zaczynamy!"%a)
        else:
            print("Nieprawidlowy wybor- musisz wybrac 1/2/3")
        #if ask_for_a_difficulty is False:
        #   print("Nieprawidlowy wybor- musisz wybrac 1/2/3")
        #else:
        #    print("Wybrales poziom: %s  ------>>> Zaczynamy!"%a)
        break    


#wyrzucanie slowa jako _ _ _ _ _
#words = ['cat', 'dog','zebra','whale','dolphin', 'giraffe', 'at']
#def pick_a_word():
#    word = random.choice(words).upper()
#    new_word = word 
#    for i in range(0, len(word)):
#        new_word = new_word.replace(word[i], ' _ ')
#    return(new_word)  
#print(pick_a_word())
#input("Odgadnij Slowo:")       



def main():
    while True:
         a = ask_for_a_difficulty(True)
         
         if not a:
            break
        
       

    pass
if __name__ == '__main__':
    main()



############################################################