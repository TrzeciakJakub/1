import signal
import time

# import sys
# import signal
# print(sys.argv[0])
# #print("Uruchomil sie")

# def ideas():
#     #print("ideas")
#     list_of_idea = []
#     if len(sys.argv) > 1 and sys.argv[0] == "--list":
#         print("1")
#         with open('ideas.txt', 'r') as f:
#             d = f.readlines()
#             for i in d:
#                 print(i)
#                 f.close()
    
        # while True:
# user_idea = input("What is Your new idea: ")
# if user_idea == "Ctrl+C":
#     print("Goodbye")
# else:
#     with open('ideas.txt', 'a+') as f:
#                     f.writelines([user_idea, "\n"])
#                     d = f.readlines()
#                     print(d)
        # else:
        #     if user_idea not in list_of_idea:
        #         list_of_idea.append(user_idea)
        #         print(list_of_idea)
        #     else:
        #         print("You have already entered that idea.")
 
def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)
 
signal.signal(signal.SIGINT, handler)
 
user_idea = input("What is Your new idea: ")
if user_idea == "Ctrl+C":
    print("Goodbye")
else:
    with open('ideas.txt', 'a+') as f:
        f.writelines([user_idea, "\n"])
        d = f.readlines()
        print(d)
