import random
def generate_otp(l):
    otp=''. join(random.choices('0123456789',k=6))
    return otp 
otp=generate_otp(1)
print(otp)
