def dupa():
    list_of_numbers = []
    i = 0
    user_list =input("jak duza lista")
    user_list_number =float(user_list)
    while i < user_list_number:
        userInput =input("Please proved Your number:")
        userInput_number = float(userInput)
        list_of_numbers.append(userInput_number)
        i += 1
    print("wystarczy juz, Twoja lista zostanie wydrukowana")
    return list_of_numbers

print(dupa())
