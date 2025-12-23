# from tabulate import tabulate

from fill import modify
from datetime import date,datetime
from info import vehicle
vehicle_obj=modify()
class user:
    def __init__(self):
        # self.vehicle_obj=modify()# import of fill.py  in given of
        pass  
    
    
    
    
    
    def issue(self,current_user):
        while(True):
            while(True):
                try:
                    check=int(input("Enter the car_id :"))
                    break
                except ValueError:
                    print("Enter the (Car_Id) in number ")
            
            
            
            found=False
            with open("issue.txt","r") as f1:
                for e in f1:
                    list1=e.strip().split(",")
                    if(list1[1]==str(check) and list1[0]==current_user):
                        found=True
                        print("One time one car rented")
                        break
            if (found==False):
            
                # (check  available or not car )
                available=(vehicle_obj.is_available(check)) # given function of fill . is_available() 
                if (available is False):
                    print("car id not found ")
                elif(available==0):# check the above 0 

                    print("Not available car ")
                else:
                    while (True):
                        try:
                            while(True):
                                while(True):
                                    str1=input("Enter the when car issue :(dd-mm-yyyy):")
                                    dt=datetime.strptime(str1,"%d-%m-%Y").date()
                                    nowdate=date.today() 
                                    check_date=(dt-nowdate).days
                                    if(check_date>=0):

                                        d=datetime.strptime(str1,"%d-%m-%Y").date()
                                        print(d)
                                        break
                                    else:
                                        print("past Date not validate")
                                break
                            
                            break
                        except ValueError:
                            print("Enter the correct data format ")
                    vehicle_obj.reduce(check)
                    with open("data.txt","r") as f2:
                        for e in f2:
                            list1=e.strip().split(",")
                            if(list1[0]==str(check)):
                                price_per_day = int(list1[2])
                                car_name=list1[1]
                                break
                            
                    # save the price in issue.txt
                    

                    with open("issue.txt","a")as f1:
                        f1.write(f"{current_user},{check},{d.strftime('%d-%m-%Y')},{price_per_day},{car_name}\n")
                    print("\n🚗----------------------------------------------------------🚗")
                    print(f"✅ Car '{check}' has been successfully issued!")
                    print(f"📅 Issue Date : {d}")
                    print(f"👤 Issued By  : {current_user}")
                    print("📅 Please remember to return it on time. Enjoy your ride! 😎")
                    print("🚗-----------------------------------------------------------🚗\n")

                    break


    # return car process  
    def returns(self,current_user):
        while(True):
            try:
                check=int(input("🚘 Enter the Car ID:"))
                break
            except ValueError:
                print("Enter the (car_ID) in number ")
        
        print()
        
        found=False
        container=[]
        with open("issue.txt","r") as f1:
            lines=f1.readlines()
        
        for line in lines:
            line=line.strip()
            if (not line):
                continue

            if(","not in line):
                continue

            uid,car_id,issue_data,price_per_day,car_name=line.split(",")
            if(uid==current_user and car_id==str(check) and  not found):

                found=True
                while (True):
                    
                    while(True):
                        try:
                            str1=input("Enter the date(dd-mm-yyyy) : ")
                            d1=datetime.strptime(str1,"%d-%m-%Y").date()
                            break
                        except ValueError:
                            print("Enter the correct date")

                    d=datetime.strptime(issue_data,"%d-%m-%Y").date()
                    days=(d1-d).days
                    print(days)

                    if days<0:#check the not less date of issue date
                       print("⚠️ You didn’t enter the return date! Please enter the correct date. 📅")
                    else:
                        if(days==0):#
                            days=1
                        
                        total=days*int(price_per_day.strip())
                        print(f"total amount of {total}")
                        print(f"Car ID           : {car_id}")
                        print(f"Car Name         : {car_name}")
                        print(f"Total days rented: {days}")
                        print(f"Total amount     : {total}")
                        
                        while True:
                            pay = input("Do you want to pay now? (yes/no): ").lower().strip()
                            if pay == "yes":
                                print("\n--- 🪙 UPI PAYMENT GATEWAY ---")
                                upi_id = input("Enter your UPI ID (e.g. user@upi): ")
                            
                                import random, time
                                otp = random.randint(100000, 999999)
                                print(f"🔐 OTP sent to your registered mobile number: {otp}")
                                try:
                                    user_otp = int(input("Enter OTP to confirm payment: "))
                                except ValueError:
                                    print("❌ Invalid input. Payment cancelled.")
                                    return
                            
                                if user_otp == otp:
                                    print("\n⏳ Processing payment...")
                                    time.sleep(2)
                                    print(f"✅ ₹{total} successfully paid via {upi_id}")
                                    print("🧾 Transaction ID:", random.randint(1000000000, 9999999999))
                                    vehicle_obj.increase(check)
                            
                                    # Remove record from issue.txt
                                    for l in lines:
                                        if l.strip() != line:
                                            container.append(l.strip())
                            
                                    with open("issue.txt", "w") as f3:
                                        for l in container:
                                            f3.write(l + "\n")
                            
                                    print("\n✅ Payment received successfully.")
                                    print("Thank you for returning the car.")
                                    print("Our representative will come to your house to collect the car and keys.\n")
                            
                                    return  # exit after payment
                                else:
                                    print("\n❌ Wrong OTP! Payment failed. Please try again.")
