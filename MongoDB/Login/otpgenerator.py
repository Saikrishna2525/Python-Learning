from random import randint

def specialOTP():
    return (
        str(randint(100, 999))
        + str(chr(randint(65, 90)))
        + str(chr(randint(65, 90)))
        + str(chr(randint(65, 90)))
    )
