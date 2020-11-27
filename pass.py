from string import printable
import random
import string

repeat = True

while repeat == True:

    # Get length of password
    length = input("Enter password length to generate. Leave blank for 12:  ")
    if length == "":
        length = 12

    # Generate Password without whitespace
    for i in range(int(length)):
        passw = random.choice(string.printable).replace("\n", random.choice(string.ascii_uppercase))
        passw = passw.replace("\t", random.choice(string.ascii_lowercase))
        passw = passw.replace("\r", random.choice(string.digits))
        passw = passw.replace(" ", random.choice(string.ascii_lowercase))
        passw = passw.replace("\f", random.choice(string.ascii_uppercase))
        passw = passw.replace("\v", random.choice(string.digits))
        print(passw, end="")
    # New line
    print()    
    # Repeat password generation?
    again = input("Regenerate? (Yes/No)").lower()
    if again == "yes" or again == "y":
        repeat = True
    else:
        repeat = False