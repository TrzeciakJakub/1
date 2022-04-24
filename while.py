#ifUserAnswered = False
#while True:
#    answer = input("What is Your Age?: ")
#    if answer: 
#        print("Your Age is: %s" % answer)
#        break
    
ifUserAnswered = False
while ifUserAnswered == False:
    answer = input("What is Your Age?: ")
    if answer: 
        if answer .isdecimal():
            ifUserAnswered = True
            print("Your Age is: %s" % answer)
        else:
            print("Your answer is wrong")


