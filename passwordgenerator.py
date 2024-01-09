import random 
import string 
import secrets 

def passwordgenerator (minimum_length,numbers=True , special_caracter=True):
    letters=string.ascii_letters
    digits=string.digits
    special_caracter=string.punctuation

    print(letters,digits,special_caracter)

passwordgenerator(10)
