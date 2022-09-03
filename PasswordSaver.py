# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:43:21 2022

@author: ericz
"""
#Variables
passwords = ["apple", "banana"]
passwordTitles = ["fruit1", "fruit2"]
validInput = 0

print("There are currently " + str(len(passwords)) + " passwords in the list")

#Function Definitions
def add_Password():
    newTitle = input("What would you like the new title of the password to be?")
    passwordTitles.append(newTitle)
    newPass = input("What would you like the new password to be?")
    passwords.append(newPass)

def view_Passwords():
    print("Your Passwords are:")
    print(passwordTitles)
    print(passwords)

while(validInput == 0):
    userYes = input("Would you like to add a new Password to the list?")
    if(userYes == "Yes" or userYes == "y" or userYes == 1):
        validInput = 1
        add_Password()
    elif (userYes == "No" or userYes == "n" or userYes == 0):
        print("you said no")
        validInput = 1
    else:
        print("Invalid Input please reply with y or n")

validInput = 0
while(validInput == 0):
    userYes = input("Would you like to view your Passwords?")
        

    