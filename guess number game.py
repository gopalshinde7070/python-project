import random
random=random.randint(1,10)
print()
print("                         **********NUMBER GUESSING GAME***********")
print()
attept=0
play=input("You are play game  (yes/no): ")
if(play=="yes"):
     while(True):
         guessnumber=int(input("GUESS THE NUMBER  : "))
         attept+=1
         if(guessnumber<random):
             print("low number")
             print()
         elif(guessnumber>random):
             print("High number")
             print()
         
         else:
             print("Congrass you are win ")
             print("secret number is: ",random)
             print("You are attempt",attept)
             break
else:
    print("please try again ")