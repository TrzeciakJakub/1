#print("""this
#is a 
#multiline
#text""")

#print("Spam" + "eggs")
#print("spam " * 3)

#x = 7
#print(x)

#print(x + 3)

#x = 7
#print(x)

#x = "This is a string"
#print(x + "!")
#print(x)

#x =input()
#print(x)

#name = input("Enter Your name: ")
#print("Hello, " + name)

#age = int(input("What is Your age:"))
#print(age)

#age = 42
#print("His age is " + str(age))

#name = input("Jak masz na imie")
#age = input("Jak masz na nazwisko")

#print(name + " is " + age)

#x =2 
#print(x)

#x += 3
#print(x)

#x = "spam"
#print(x)

#x += "eggs"
#print(x)

#num = int(input())
#print(num)

#print(num:=int(input()))

#x = 3
#num = 17
#print(num % x)

#x = int(input("wpisz x"))
#y = int(input("wpisz y"))
#sum = x + y
#print(sum)

#my_boolean = True
#print(my_boolean)
#True

#print(2 == 3)
#False

#print("hello" =="hello")
#True

#print(2 == 3)

#if 10 > 5:
 #   print("10 greater than 5")
#print("Program ended")

#spam = 7
#if spam > 5:
#   print("five")
#if spam > 8:
#   print("eight")

#x = 1, 2, 3
#if x == 1:
#    print("yes")
#else:
#    print("no")

#num = (input("Podaj Cyfre"))
#if num == "1":
#    print("One")
#else:
#    if num == "2":
#        print("Two")
#    else:
#        if num == "3":
#            print("Three")
#        else:
#            print("Something Else")

#str ="Hello World!"
#print(str[6])

#nums = [7, 7, 7, 7, 7]
#nums[2] = 5
#print(nums)

#nums = [1, 2, 3, 4, 5]
#nums[3] = nums[1]
#print(nums[3])

#nums = [1, 2, 3]
#print(nums + [4, 5, 6])
#print(nums * 3)


#words = ["spam", "egg", "spam", "sausage"]
#print("spam" not in words)
#print("egg" not in words)
#print("dog" not in words)




#nums = [1, 2, 3]
#nums.append(4)
#print(nums)


#nums = [1, 2, 3]
#print(len(nums))

#words = ["Python", "fun"]
#index = 0
#words.insert(index, "is")
#print(words)


#letters = [ "p", "q", "r", "s", "p", "u"]
#print(letters.index("r"))
#print(letters.index("p"))
#print(letters.index("z"))

#i = 1
#while i <=5:
#    print(i)
#    i = i + 1
#print("Finished!")


#x = 1
#while x < 10:
#    if x%2 == 0:
#        print(str(x) + " is even")
#    else:
#        print(str(x) + " is odd")
#    x += 1

#x = 1
#x%2 == 0
#print(str(x))


#i = 0
#while True:
#    print(i)
#    i = i + 1
#    if i >= 5:
#        print("breaking")
#        break
#print("Finished")


#i = 0
#while i<5:
#    i += 1
#    if i == 3:
#        print("skipping 3")
#    continue
#print(i)

#words = ["hello", "world", "spam", "eggs"]
#for word in words:
#    print(word + "!")

#str = "testing for loops"
#count = 0
#for x in str:
#    if(x =="t"):
#        count += 1
#print(count)

#numbers = list(range(10))
#print(numbers)

#numbers = list(range(3,8))
#print(numbers)
#print(range(20) == range(0,20))


#nums = list(range(3, 15,3))
#print(nums[2])

#for i in range(5):
#    print("hello!")

#list = [1, 1, 2, 3, 5, 8, 13]
#print(list[list[4]])

#for i in range(10):
#  if not i % 2 == 0:
#    print(i+1)

#list = [1, 2, 3]
#for word in list:
#    print(word)

#print("Hello world!")
#range(2, 20)
#str(12)
#range(10, 20, 3)



#def my_func():
#    print("spam")
#    print("spam")
#    print("spam")
#
#my_func()

#def print_with_exclamation(word):
#    print(word + "!")
    
#print_with_exclamation("spam")
#print_with_exclamation("eggs")
#print_with_exclamation("python")

#ef print_sum_twice(x,y):
#    print(x + y)
#    print(x + y)

#print_sum_twice(5,8)

#def even(x):
#    if x % 2 == 0:
#        print("yes")
#    else:
#        print("no")
#even(1)

#def max(x, y):
 #   if x <=y:
 #       return x
#    else:
#        return y

#print(max(4, 7))
#z = max(8, 5)
#print(z) 


#def shout(word):

#   """
#
#dupa dupa
#cycki 
#"""
#    print(word + "!")
#shout("spam")

#def multiply(x, y):
#    return x * y
#a = 4
#b = 7
#operation = multiply
#print(operation(a, b))

#def add(x, y):
#    return x + y
#def do_twice(func, x, y):
#    return func(func(x, y), func(x, y))

#a = 5
#b = 10
#print(do_twice(add, a, b))

#def square(x):
#    return x * x
#def test(func, x):
#    print(func(x))

#test(square, 42)

#import random
#for i in range(5):
#    value = random.randint(1, 6)
#    print(value)

#from math import pi
#print(pi)

#from math import sqrt as square_root
#print(square_root(100))

#def print_nums(x):
#    for i in range(x):
#        print(i)
#        return
#print_nums(10)

#def func(x):
#    res = 0
#    for i in range(x):
#        res += 1
#    return res
#print(func(4))

#try:
#     num = 5 / 0
#except: 
#    print("AN error occured")
#    raise 

#print(1)
#assert 2 + 2 == 4
#print(2)
#assert 1 + 1 == 3
#print(3) 

#temp = -10
# assert (temp >= 0), "Colder than absolute zero"

