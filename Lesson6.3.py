#Libraries
import time

#Functions
def encryptor(phrase):
    encrypted_phrase = ""
    for letter in phrase:
        n = ord(letter)
        n2 = n + key
        encrypted_c = chr(n2)
        encrypted_phrase = encrypted_phrase + encrypted_c
    return encrypted_phrase

#Variables
key = 555

#Main
password = input("Type the password to start encrypting:")

if password == "key555":
    user_word = input("Type something to encrypt: ")

    encrypted_word = encryptor(user_word)
    print(encrypted_word)
    
else:
    print("Wrong Password")
    time.sleep(1)
    print("Closing in 3")
    time.sleep(1)
    print("Closing in 2")
    time.sleep(1)
    print("Closing in 1")
    time.sleep(1)
    exit

##unencrypted = input("Give me a letter:")
##
##unencrypted = ord(unencrypted)
##
##encrypted = unencrypted + key
##
##encrypted = chr(encrypted)
##print(encrypted)
