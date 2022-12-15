import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!#%&/()=@£$€[]}"
password = ""
while 1:
    
    while True:
        try:
            password_length = int(input("how long is your password:"))
            if password_length <= 0:
                password_length = 8
        except ValueError:
            print("that is not an acceptable number, here is a password anyway")
            password_length = 8
        break
    
    for x in range(0,password_length):
        password_char = random.choice(chars)
        password = password + password_char

    
    print("here is your password:",  password)
    break                      
