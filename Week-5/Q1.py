import random as r

def generate_otp():
    return r.randint(1,999999)

print("Secure OTP:", generate_otp())
