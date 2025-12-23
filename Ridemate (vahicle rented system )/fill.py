from tabulate import tabulate
from info import vehicle
class modify:
    def __init__(self):
        self.modify=""
    
    def add(self):
        while(True):
            while (True):
                try:

                    id=int(input("🆔  Enter Car ID (numeric, e.g., 101):"))
                    break
                except ValueError:
                    print("Enter the Car ID only number allow ")
            
            # --------check dupli--------
            found=False
            with open("data.txt","r") as f2:
                for e in f2:
                    list1=e.strip().split(",")
                    if(list1[0]==str(id)):
                        found=True
                        print("ID already exit take another Id  ")
                        break
            
            #-------duplicate no then create car             
            if  found==False:
                    name=input("🏷️  Enter the Car Name: ")
                    while(True):
                        try:
                            price=int(input("💰  Enter the Car Price (only numbers):"))
                            break
                        except:
                            print("Enter the price only number ")
                    while(True):
                        try:
                        
                            available=int(input("📦  Enter the Available Cars (e.g., 10, 5, 2): "))
                            break
                        except ValueError:
                            print("Enter the car available only number ")
                    e=vehicle(id,name,price,available)
                    with open("data.txt","a") as f1:
                        f1.write(str(e)+"\n")
                        print("✅  Car Details Added Successfully!")
                        break
                        

                        

    def show(self):
        container=[]
        with open("data.txt","r") as f1:
            for s in f1:
                list1=s.strip()
                if list1=="":
                    continue
                container.append(list1.split(","))
        
        headers=["Car_Id","Car_Name ","price(per_day)","Car_Available"]
        print(tabulate(container,headers=headers,tablefmt="fancy_grid"))

    
    def serach(self):
        while(True):
            try:

                id=int(input("Enter the Search (Car Id ) Number: "))
                break
            except ValueError:
                print("Enter the car id only in number ")
        contianer=[]
        with open("data.txt","r") as f1:
            for e in f1:
                list1=e.strip().split(",")
                if(list1[0]==str(id)):
                   
                    contianer.append(list1)

                    head=["CAr_Id","Car_Name","Price(Per_day)","Car_Available"]
                    print(tabulate(contianer,headers=head,tablefmt="fancy_grid"))
                    
                    break
            else:
                print("Not found the number ")
    
    def update(self):
        container=[]
        found=False
        while(True):
            try:
                id=int(input("🆔 Enter the Car ID:"))
                break
            except ValueError:
                print("Enter the Correct (car_ID)")        
       
        with open("data.txt","r") as f1:
            for e in f1:
                list1=e.strip().split(",")
                if(list1[0]==str(id)):
                    found=True
                    print("1️⃣. 🏷️  Name ")
                    print("2️⃣. 💰  Price")
                    print("3️⃣. 📦  Availability")
                    while (True):
                        try:

                            ch=int(input("➡️  Choose the detail you want to update:"))
                            break
                        except ValueError:
                            print("Enter the number(1-3)")
                    if(ch==1):
                        name=input("🚗  Enter the Name of the Car:")
                        list1[1]=name
                    elif(ch==2):
                        while(True):
                            try:
                                price=int(input("💰  Enter the Price of the Car (₹):"))
                                break
                            except ValueError:
                                print("Enter the (price) in number ")

                        list1[2]=str(price)
                    elif(ch==3):
                        while(True):
                            try:

                                av=int(input("📦  Enter the Number of Cars Available:"))
                                break
                            except:
                                print("Enter the available in Number ")
                        list1[3]=str(av)
                    print("✨  Update Completed! Your data has been saved. 🚗")
                e=(",").join(list1)+"\n"
                container.append(e)
        if found==False:
            print("Not found ")
        else:
            with open("data.txt","w") as f1:
                for e in container:
                    f1.write(e)
                    
                    
    
    def delete(self):
        container=[]
        while(True):
            try:
                id=int(input("🔹  Enter Car Identification Number (Car_ID):"))
                break
            except ValueError:
                print("Enter the Car_ID in number ")
        found=False
        with open("data.txt","r") as f1:
            for e in f1:
                list1=e.strip().split(",")
                if(list1[0]==str(id)):
                    found=True
                    continue # skip the line to delete it
                container.append(e)

        if found==False:
            print("Not found in file")
        else:
            with open ("data.txt","w") as f1:
                for e in container:
                    f1.write(e)
                print("✅  Deletion Successful — The record has been removed.")
                    
    
    # in the there count number
    def is_available(self,check):
        with open("data.txt","r") as f1:
            for s in f1:
                list1=s.strip().split(",")
                if(list1[0]==str(check)):
                    return int(list1[3]) # return given number how much raimaning in the class user info/issue()
        return False
    
    def reduce(self,check):
        container=[]
        found=False
        with open("data.txt","r") as f1:
            for e in f1:
                list1=e.strip().split(",")
                if(list1[0]==str(check)):
                    found=True
                    available=int(list1[3])
                    if( available>0):
                        list1[3]=str(available-1)
                    else:
                        print("Not car available")
                
                e=",".join(list1) +"\n"
                container.append(e)
        
        # in the there update date 
        if found:
            with open("data.txt","w") as f1:
                
                for s in container:
                    f1.write(s)
        else:
            print("Not found car ")
                



    def increase(self,check):
        
        container=[]
        found=False
        with open("data.txt","r") as f1:
            for s in f1:
                list1=s.strip().split(",")
                if(list1[0]==str(check)):
                    found=True
                    available=int(list1[3])
                    list1[3]=str(available+1)
                e=",".join(list1)+"\n"
                container.append(e)
        
        # If car was deleted, re-add it with 1 available
        if not found:
            with open("issue.txt","r") as f1:
                for e in f1:
                    list1=e.strip().split(",")
                # print("Car was deleted. Restoring it with 1 available.")
                container.append(f"{check},{list1[4]},{list1[3]},0\n")
        
        with open("data.txt","w") as f1:
            for s in container:
                f1.write(s)
    
