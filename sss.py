import random

print("")
tekst = "HangMan Game\n"
print(tekst.center(80))
tekst2 = "Wybierz Poziom Trudnosci\n"
print(tekst2.center(80))
print("1 = Latwy   \n2 = Sredni \n3 = Trudny \n")


def is_number(userInput):
    value = str(userInput)
    if value.isdecimal(): 
    #value = int(userInput)
    #if (value >=1 and value <=3):
        return True
    else: 
        return False
    pass


def ask_for_a_difficulty(forceValidInput):
    while True:
        a = input("Wybieram Poziom: ")
        a_difficulty = is_number(a)
        if a_difficulty is False:
            print("Nieprawidlowy wybor- musisz wybrac 1/2/3")
        else:
            print("Wybrales poziom: %s  ------>>> Zaczynamy!"%a)

words = ['cat', 'dog','zebra','whale','doplhin']
def pick_a_word():
    word_position = random.randint(0, len(words) -1)
    return words[word_position]
print(pick_a_word())         



def menu():
    while True:
        a = ask_for_a_difficulty(True)
        if not a:
            break
       

    pass
if __name__ == '__main__':
    menu()

    

#words = ["dog", "cat", "elephant", "rabbit", "mouse", "horse", "hamster", "giraffe", "snake", "gepard", "duck", "antelope", "hippo", "apple", "pizza", "strawberry", "milk", "spaghetti", "mayonnaise", "juice", "chocolate", "scissors", "ball", "computer", "headphones", "microwave", "fridge", "programmer", "hairdresser", "doctor", "engineer", "restaurant", "library", "museum", "cinema", "game", "guitar", "bike", "skateboard", "piano"]

#def get_world(words):
#    word = random.randint(0, len(words) -1)
#    print(word)



#def menu():
#    while True:
#        a = ask_for_a_difficulty(True)
        
       

#    pass
#if __name__ == '__main__':
#    menu()
