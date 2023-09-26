import random

print("Enter username and password")
n=0
def main():
    global n
    
    username=input("Enter username :")
    password=input("Enter password :")
    
    
    if username!="Danishkhan" or password!="Danish123":
        n=n+1
        if n<3:
            print("please Try Again..!")
            main()
        else:
            print("sorry..! you have reached maximum attempts")
        
    
        
    else:      
        otp=random.randint(1111,9999) 
        print("Your otp is : ",otp)
    
        Enter_otp=int(input("Enter otp :"))
        
        if otp == Enter_otp:
            print("Login successfull..!")
            
        else:
            print("Incorrect OTP , Please try again...!")
        
main()