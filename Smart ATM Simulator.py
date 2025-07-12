print(" ***********  ***************WELCOME********************* **********                                                                           ")
print( "                         💕 BANK OF INDIA 💕                                      ")
balance=12000

for i in range(0,3):
    password=input("Enter password : ")
    if(password=="1234"):
        print()
        print("login succesfully")
        print()
        while True:
             print(""" option for you : 
             1.check Balance
             2.withrow Balance
             3.deposit money    
             4.Exit  """)
                   
             print()
             option=int(input("select option: "))

             if(option==1):
                 print("Balance : ",balance)
                 print()
             elif(option==2):
                 withdraw=int(input("withdraw :₹ "))
                 print()
                 if(withdraw<balance):
                     print("Withdraw succesful.")
                     balance-=withdraw

                     print("your raimaing balance :₹",balance)
                     print()
                 else:
                     print("Not suffecient balance : ")    
                     print("Your Bank Balance :₹",balance)
                     print()
             elif(option==3):
     
                 deposit=int(input("Deposit amount :₹"))
                 print("Deposit Succesful.")
                 balance+=deposit
                 print("balance:₹",balance)
                 print()
             elif(option==4):
                 print("Thank you for visting ATM ")
            
            
                 break
             else:
                 print("Invalid option")
                 break
        break
                
    else:
        print("Enter correct password ")
if(password!="1234"):
    print("Blocked your account")