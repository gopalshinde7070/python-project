
import re#regular expression for  password or userid,in given requrment
import pwinput # user in on screen hide password
import hashlib # hide of in file txt
import base64  # hide of in file txt user name or password
from geopy.geocoders import Nominatim # for the location search
import time

from fill import modify
from sign_in import Sign_in
from userinfo import user

up=user()
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')
print("="*60)
print("🚗  WELCOME TO RIDEMATE CAR RENTAL SYSTEM  🚗".center(60))
print("="*60)
print("\nDrive your dream car, anytime, anywhere!\n")
time.sleep(2)
    
c=modify()
while(True):
    print("_-_-"*30)
    print("\n")
    print("1️⃣  Admin")
    print("2️⃣  User")
    print("3️⃣  Exit")
    print("\n")
    print("=^=^"*30)
    while(True):
        try:
            ask=int(input("Enter the above option : "))
            break
        except ValueError:
            print("Enter only Number (1-3)")
    
   
    if ask == 1:
        
        print("╔" + "═"*58 + "╗")
        print("║" + "🚘  SWIFTRIDE CAR RENTAL SYSTEM  🚘".center(58) + "║")
        print("╠" + "═"*58 + "╣")
        print("║" + "🔐  USER LOGIN PORTAL".center(58) + "║")
        print("╚" + "═"*58 + "╝")
        attempts = 0
        while attempts < 3:
            ui = input("Enter the User_name : ")
            ps = pwinput.pwinput(prompt="Enter the password : ", mask="*")
            print("checking account…")
            time.sleep(1)
    
            with open("admin.txt","r") as f:
                ad_user, ad_pass = f.read().strip().split(",")
    
            if ui == ad_user and ps == ad_pass:
                # successful login → show your existing menu
                
                print("="*65)
                print("🛠️  ADMIN PANEL — SWIFTRIDE CAR RENTAL SYSTEM  🛠️".center(65))
                print("="*65)
                print("\nManage your fleet efficiently and effortlessly!\n")
                print("-"*65)
                while True:
                    
                    print("-"*65)
                    print("1️⃣  Add Car")
                    print("2️⃣  Show Cars")
                    print("3️⃣  Search Car")
                    print("4️⃣  Update Car Details")
                    print("5️⃣  Delete Car")
                    print("6️⃣  Exit")
                    print("7️⃣  Change Admin Password")
                    print("-"*65)
                    time.sleep(2)
                    while True:
                        try:
                            ch = int(input("Enter the choice : "))
                            
                            break
                        except ValueError:
                            print("Enter only number ")
    
                    if ch == 1:
                        c.add()
                    elif ch == 2:
                        c.show()
                    elif ch == 3:
                        c.serach()
                    elif ch == 4:
                        c.update()
                    elif ch == 5:
                        c.delete()
                    elif ch == 6:
                        break
                    elif ch == 7:
                        old = pwinput.pwinput("Enter old password: ",mask="*")
                        if old == ad_pass:
                            newp = pwinput.pwinput("Enter new password: ",mask="*")
                            with open("admin.txt","w") as f:
                                f.write(f"{ad_user},{newp}")
                            print("✅ Password changed successfully!")
                            ad_pass = newp
                        else:
                            print("❌ Wrong old password")
                    else:
                        print("Enter the correct option ")
                break  # exit login attempts loop after success
            else:
                attempts += 1
                if attempts < 3:
                    print(f"❌ Wrong credentials, try again ({3 - attempts} attempts left)")
                else:
                    print("❌ You have tried 3 times. Try later...")
    

    elif(ask==2):
       
        print("_-_-"*30)
        print("="*65)
        print("👤  USER PORTAL — RIDEMATE CAR RENTAL SYSTEM".center(65))
        print("="*65)
        print("\n")
        print("1️⃣  Login")
        print("2️⃣  Register ")
        print("3️⃣  Exit")
        print("\n")
        print("=^=^"*30)
        while(True):
            try:

                ch=int(input("➡️  Enter your choice: "))
                break
            except ValueError:
                print("Enter the correct option(1-2) in number")
        if(ch==1):
            found=False
            for i in range(1,4):
                uname=input("👤 Enter Your Username:")
                u=hashlib.sha256(uname.encode()).hexdigest()

                p=pwinput.pwinput(prompt="🔐  Enter Your Password:",mask="*")
                pw=hashlib.sha256(p.encode()).hexdigest()
                print("checking account…")
                time.sleep(1)
                with open("login.txt","r") as f1:
                    for e in f1:
                        list1=e.strip().split(",")
                        if(list1[0]==u and list1[1]==pw):
                            found=True
                            current_user=uname
                            while(True):
                                print("-_-_"*30)
                                print("\n")
                                print("---------------------Car Rented System----------------- ")
                                print("1️⃣  Rent a Car")
                                print("2️⃣  Return a Car")
                                print("3️⃣  Exit")
                                print("\n")
                                print("=^=^"*30)
                                while(True):
                                    try:
                                        ch=int(input("Enter the above option"))
                                        break
                                    except ValueError:
                                        print("Enter the correct option(1-4)")
                                
                                    
                                if(ch==1):
                                    
                                    c.show()
                                    
                                    time.sleep(2)
                                    up.issue(current_user)
                                elif(ch==2):
                                    up.returns(current_user)
                                elif(ch==3):
                                    print("Thank You")
                                    break

                            break
                if  (found):
                    break
                else:
                    print("TRY AGIAN")

            if (not found):
                print("sorry your are try later....")    



        elif(ch==2):
            # name of user
            print("Enter the current name (Only Alphabet),(starting not space),(above 1 name or less 4)")
            while(True):
                nm=input("Enter the name: ")
                if(re.findall(r"^[A-Za-z]",nm) and not re.findall(r"[0-9]",nm ) and len(nm.split())>1 and len(nm.split())<4):
                    name=nm
                    break
                else:
                    print("this is not given name ")
            # Age of user
            while(True):
                try:
                    ag = int(input("Enter your age (18-80): "))
                    if(ag>=18 and ag<80):
                        age=ag
                        break
                    else:
                        print("Age not allowed below 18 or above 80")

                except ValueError:
                    print("Invalid input! Please enter numbers only.")


            # location 
            
                   
            address=input("Enter the Address : ")
                    
                
            while(True):
                dri=input("💡 Please enter a valid 10-digit mobile number (e.g. 9876543210) ")
                if re.findall(r"^[6-9]\d{9}$", dri):
                    mobile=dri
                    break
                else:
                    print("Enter a valid 10-digit mobile number without spaces.")



            # User_Name
            while(True):
                while(True):
                    print("\n💡 Username can include both letters ,numbers, and length above 5 (e.g. admin123)\n")
                    id=input("enter the user_id : ")
                    if(re.findall(r"^[A-Za-z0-9]",id)and re.search(r"[0-9]",id) and not re.search(r"\s",id) and len(id)>=5):
                        ids=id
                        break 
                    else:
                        print("Enter the valid User Id name ")
                encode_id=hashlib.sha256(ids.encode()).hexdigest()

                #-----check user id duplication
                found=False
                with open("login.txt","r") as f1:
                        for e in f1:
                            list1=e.strip().split(",")
                            if(list1[0]==encode_id):
                            
                                print("This is account already exit please choice different (USer name )")
                                found=True
                                break
                                
                


                if found==False:
                    uid=encode_id
                    break


            # password
            while (True):
                print("Enter a password: min 8 chars, at least 1 number, 1 lowercase, 1 uppercase, 1 special symbol(eg @#$!%^&*), eg (Pass@1234)")

                pa=input("Enter the password : ")

                if(re.findall(r"^[A-Za-z0-9]",pa )and re.findall(r"[0-9]",pa) and re.findall(r"[!@#$%^&*()_+-={}:;'<>,.?/]",pa)and re.findall(r"[A-Z]",pa)and len(pa)>5 and len(pa)<17):
                    pas=hashlib.sha256(pa.encode()).hexdigest()
                    break
                else:
                    print("Enter a password: min 8 chars, at least 1 number, 1 lowercase, 1 uppercase, 1 special symbol")

            a=Sign_in(uid,pas,name,age,mobile,address)

            with open ("login.txt","a") as f1:
                f1.write(str(a)+"\n")
                print("\n")
                print("✨" * 40)
                print("🎉  REGISTRATION SUCCESSFUL!  🎉".center(80))
                print("✨" * 40)
                print("\n✅ You have been successfully registered in the system.")
                print("🚗 Welcome to the Car Rental Family! Enjoy your ride 😎")
                print("\n")
                print("✨" * 40)

    elif(ask==3):
        print("\n")
        print("🌟" * 50)
        print("🙏  THANK YOU FOR VISITING  🙏".center(100))
        print("🚗  RIDEMATE CAR RENTAL SYSTEM  🚗".center(100))
        print("🌟" * 50)
        print("\n💖 We appreciate your time! Hope to see you again soon. Safe travels! ✨")
        print("\n")
        print("🌟" * 50)

        break

    else:
        print("Enter The correct option")