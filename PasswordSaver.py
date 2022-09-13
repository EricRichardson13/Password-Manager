# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 15:43:21 2022

@author: Eric Richardson
"""
#imports
import csv
import os.path

#Variable Declaration
passwords = ["Password"]
passwordTitles = ["Title"]
validInput = 0

print("There are currently " + str(len(passwords)) + " passwords in the list")

#Files
filename = "ENR_passwords.csv"
password_exists = os.path.exists(filename)

#Function Definitions

# Function that begins the program that either creates the file or loads it
def begin_prog(pwT, pw):
    if(password_exists): 
        with open(filename, mode ='r') as file:
            csvFile = csv.reader(file)
            csvList = list(csvFile)
            pwT = csvList[0]
            pw = csvList[1]
            print("Password file exists, printing")
            print(pwT)
            print(pw)
            return pwT, pw
    else:
        with open(filename, 'w', newline ='') as csvfile: 
        # creating a csv writer object
            csvwriter = csv.writer(csvfile) 
            # writing the fields 
            csvwriter.writerow(passwordTitles) 
            # writing the data rows 
            csvwriter.writerow(passwords)
            print("Password File doesn't exist, creating")
            print(passwordTitles)
            print(passwords)
            return passwordTitles, passwords

#Add a new password to the list and update the local list
def add_Password():
    newTitle = input("What would you like the new title of the password to be?")
    passwordTitles.append(newTitle)
    newPass = input("What would you like the new password to be?")
    passwords.append(newPass)
    print(passwordTitles)
    print(passwords)
    return passwordTitles, passwords

#View passwords currently in the list
def view_Passwords():
    print("Your Passwords are:")
    print(passwordTitles)
    print(passwords)

#Save the passwords to the file
def save_Passwords():
    with open(filename, 'w+', newline ='') as csvfile: 
    # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        # writing the fields 
        csvwriter.writerow(passwordTitles) 
        # writing the data rows 
        csvwriter.writerow(passwords)
        print("Saving Passwords.")
        print(passwordTitles)
        print(passwords)
        return passwordTitles, passwords


# -------------------------------
# BEGIN RUNNING PROGRAM
# -------------------------------

# Begin program by loading from the file
passwordTitles, passwords = begin_prog(passwordTitles, passwords)

#Ask user what they want to do
while(validInput == 0):
    userYes = input("Would you like to add a new Password to the list?")
    if(userYes == "Yes" or userYes == "y" or userYes == 1):
        validInput = 1
        passwordTitles, passwords = add_Password()
        add_Password()
    elif (userYes == "No" or userYes == "n" or userYes == 0):
        print("you said no")
        validInput = 1
    else:
        print("Invalid Input please reply with y or n")

validInput = 0

# Ask user what they want to do again
while(validInput == 0):
    userYes = input("Would you like to view your Passwords?")
    if(userYes == "y"):
        view_Passwords()
        validInput = 1

passwordTitles, passwords = save_Passwords()
print("Program End")
        

    