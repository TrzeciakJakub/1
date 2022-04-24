print("Hello World")
a = 5
b = 10
if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("False")
a = 50
b = 50
if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("False")

a = 5
b = 50
if a < b:
    print(str(a) + "<" + str(b))
    print("%s > %s" % (a,b))
elif a > b:
    print("a > b")
else:
    print("False")