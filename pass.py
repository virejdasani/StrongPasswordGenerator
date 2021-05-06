"""
Strong Password Generator [Python3]

This tool is written in python3, and serves the feature of generating strong passwords for the user to use. First off, we all know that for better security, we always should keep a hard passwords either on our phones, computers or on our social media accounts. This script when run, asks for the length of the to-be generated password. And, then it proceeds to generate the random characterized password. The characters that could be in the password string, would be all the alphanumeric characters as well as the special characters. This tool can be run using this command on the terminal : python3 pass.py

Author : Virej Dasani (https://github.com/virejdasani/)
Created on : Nov 27, 2020

Last modified by : Rishav Das (https://github.com/luckyverma-sudo)
Last modified on : May 6, 2021

Changes made in last modification :
1. Changed the code structure and removed the requirements of some modules (string).
2. Removed many errors that can be caused if the script / tool is not handled properly
3. Added commented docs to the script file + added comments inside the code too, to make this script file more attractive and easily understandable for the beginners and program readers.

Authors contributed to this script (Add your name below if you have contributed) :
1. Virej Dasani (github:https://github.com/virejdasani/)
2. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
from random import choices

def generatePassword(length):
    """ The function generates a random password using the alphanumeric characters and the special characters. The function requires one argument : length. The length is to be mentioned in numeric format. The function also requires the 'choices' function which is defined in the 'random' library. So, we need the choices function of the random library to be imported in the script where the function is to be used. Add this code to the script file for importing the 'choices' function : from random import choices. """

    # The set of characters from which password will be crafted
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=+*!@#$%&~:;,.?/[]()\'"'

    # Creating the password in a loop
    password = ''
    while len(password) != length:
        # Looping until the password does not hit the user specified characters length

        password += choices(characters)[0]
    return password

def main():
    # Displaying the name of the script
    print('\t[  Password Generator ]\n[ Available at : https://github.com/virejdasani/StrongPasswordGenerator/ ]\n')

    # Asking the user to enter a desired password length
    length = input('Enter a proper password length [leave blank for 12] : ')

    # Checking wheter the user entered password length is less than 8 or not
    if len(length) == 0:
        # If the user entered a blank value, then we go for default 12 as a value

        # Generating the password
        password = generatePassword(12) 
    elif len(length) < 8:
        # If the user entered password length is less than 8

        input('[ Error : The password should be atleast of 8 characters for ensuring proper security ]\nPress enter key to continue...')
        return 0
    else:
        # If the user entered password length is equal or more than 8

        # Generating the password
        password = generatePassword(int(length))
    
    # After we reach upto here, we display the generated password on the console screen
    input(f'[$] Password generated : {password}\nPress enter key to continue...')
    return 1

if __name__ == '__main__':
    while True:
        try:
            main()
            print('\n[ ------------------ NEW GENERATION ------------------- ]\n')
        except KeyboardInterrupt:
            # If the user presses CTRL+C key combo, then we exit the script

            exit()
        except Exception as e:
            # If there are any errors in the process, then we display the error on the console screen

             input(f'[ Error : {e} ]\nPress enter key to continue...')
             exit()
