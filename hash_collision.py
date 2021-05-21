import hashlib
import os
import random


def hash_collision(k):
    if not isinstance(k, int):
        print("hash_collision expects an integer")
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
        
    #Collision finding code goes here
    char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+:|<>?/.,'
    x_end = 0
    y_end = 1
    x = b'\x00'
    y = b'\x00'
    x_txt = ''
    y_txt = ''
    while x_end != y_end:
        if random.randint(0, 1) == 0:
            x_txt += random.choice(char_list)
            x = x_txt.encode('utf-8')
        else:
            y_txt += random.choice(char_list)
            y = y_txt.encode('utf-8')

        shax = hashlib.sha256(x).digest()
        shay = hashlib.sha256(y).digest()

        x_end = int(shax.hex(), 16) % 2**k
        y_end = int(shay.hex(), 16) % 2**k

    # while x_end != y_end:
    #     x_txt += random.choice(char_list)
    #     x = x_txt.encode('utf-8')

    #     y_txt += random.choice(char_list)
    #     y = y_txt.encode('utf-8')
        
    #     shax = hashlib.sha256(x).digest()
    #     shay = hashlib.sha256(y).digest()

    #     x_end = int(shax.hex(), 16) % 2**k
    #     y_end = int(shay.hex(), 16) % 2**k

    return(x, y)


# (x, y) = hash_collision(5)
# shax = hashlib.sha256(x).digest()  # mod (2^1)
# shay = hashlib.sha256(y).digest()  # % (2^1
# print(x)
# print(bin(int(shax.hex(), 16)))
# print(y)
# print(bin(int(shay.hex(), 16)))
