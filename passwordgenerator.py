import random 
import string 
import secrets 

def passwordgenerator (minimum_length,numbers=True , special_character=True):
    letters=string.ascii_letters
    digits=string.digits
    special_character=string.punctuation
 
    characters= letters
    if numbers:
         characters += digits
    if special_character:
         characters += special_character 

    pwd = ""        
    meets_criteria = False 
    has_number = False
    while not meets_criteria or len(pwd)< minimum_length :
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits : 
            has_number = True 
        elif new_char in special_character:
            has_special = True 
                
        meets_criteria = True 
        
        if numbers:
            meets_criteria = has_number
        if special_character:
            meets_criteria = meets_criteria and has_special
            
        return pwd             


pwd = passwordgenerator (10)
min_length = int(input("Enter the minimum length: "))
has_number=input("do you want to have numbers(y/n) ?").lower()=="y"
has_special=input("do you want to have numbers(y/n) ?").lower()=="y"
pwd = passwordgenerator(min_length,has_number,has_special)
print(pwd)

         