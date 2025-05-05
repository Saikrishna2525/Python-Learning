from random import randint
def generateOTP():
    OTP = randint(1000, 9999)
    return OTP
if __name__ == '__main__':    
    input("Press Enter to generate OTP...")
    print(f"Your OTP is {generateOTP()}")
