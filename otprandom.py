import random
otp=random.randint(100000,999999)
print("otp:",otp)
user_otp=int(input("enter the otp:"))
if otp==user_otp:
    print("login")
else:
    print("denied")