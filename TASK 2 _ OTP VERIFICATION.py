import os                # This is used for system function
import math          # The math library
import random     # For random numbers
import smtplib      # For email functions
digits = "0123456789"
OTP = ""

for i in range (6):
    OTP +=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
message = otp

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
emailid = input("Enter your email: ") 
s.login("akshathaveeraragavan@gmail.com", "etzmxtfnsdqwvlxl") # send the otp via your mail
s.sendmail('&&&&&&',emailid,message)

a = input("Enter your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
