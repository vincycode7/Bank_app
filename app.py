#import needed Libraries
from Banking_app.Bankingapp import Bankingapp
import os
import time

usr = dict()
emails = list()

if __name__ == "__main__":


    while True:
        #clear screen
        os.system("reset")
        
        #display message
        print('Press 1: create account \nPress 2: transaction \nPress 0: Exit')

        # accept input
        try:
            reply = int(input('\nEnter Respnse :- '))
        except:
            print('Integer required')
            continue

        #create account or make Transactions
        if reply == 0:
            exit(0)
        elif  reply== 1:
            #clear screen
            os.system("reset")

            #accept input
            Name = input("Enter Name:- ")
            Email = input("Enter Email:- ")
            Passwrd = input("Enter Password:- ")

            if Email in emails:
                print('\nEmail has been Used by Another User, Pick a new one')
                input('Press Enter to Continue')
                continue

            #creare user account
            user = Bankingapp(Name, Email, Passwrd)

            #add user to active users
            usr[user.unique_id] = user

            #add email to active emails
            emails.append(user.email)

            #clear screen
            os.system("reset")

            #print user details
            #clear screen
            os.system("reset")
            
            #message
            print(f'Account Succesfully Created -- your Unique is is {user.unique_id} remember it for later login\n')
            _ = input('Press any key to continue')
            continue
        elif reply == 2:
            #open the database file or create if it doesn't exit
            # try:
            #     dbase = open('dbase.txt','r')
            # except:
            #     #file not found creat file
            #     dbase = open('dbase.txt','w')

            #clear screen
            os.system("reset")

            #accept input
            uni_id = int(input("Enter Unique Id:- "))
            Passwrd = input("Enter Password:- ")

            #check login credentials
            if uni_id in usr.keys() and Passwrd == usr[uni_id].passwrd:
                user = usr[uni_id]
                #clear screen
                os.system("reset")

                print(f'\nWelcome {user.name}\n')
                print("Press 1:- check balance \nPress 2:- deposit \nPress 3:- withdraw Press \nPress 4:- transfer\n")

                #accept input
                reply = int(input("Enter Response:- "))

                #check balance
                if reply == 1:
                    #clear screen
                    os.system("reset")

                    print(f"Your remaining Balance is {user.check_balance()}")
                   
                    _ = input('Press any key to continue')
                    continue

                #deposit
                elif reply == 2:
                    #clear screen
                    os.system("reset")

                    reply = int(input("Enter Amount:- "))

                    if reply < 0:
                        print('\namount should be greater than or equal to zero\n')
                        _ = input('Press any key to continue')
                        continue

                    elif reply >= 0:
                        status = user.deposit(amount=reply)
                        if status == 1:
                            print("Transaction Successful")
                            usr[user.unique_id] = user
                        # else:
                        #     print("Transaction Failed, Insufficient Balance")
                        
                        _ = input('Press any key to continue')
                        continue

                    else:
                        print("Invalid amount, try again")
                        _ = input('Press any key to continue')
                        continue
                
                #withdraw
                elif reply == 3:
                    #clear screen
                    os.system("reset")

                    reply = int(input("Enter Amount:- "))
                    status = user.withdraw(amount=reply)

                    if status == 1:
                        print("Transaction Successful")
                        #add user to active users
                        usr[user.unique_id] = user

                    else:
                        print("Transaction Failed, Insufficient Balance")
                    
                    _ = input('Press any key to continue')
                    continue

                #transfer
                elif reply == 4:
                    #clear screen
                    os.system("reset")

                    to_usr_id = int(input("Enter Unique Id Of Recipient:- "))
                    to_usr_email = input("Enter Recipient Email:- ")
                    amount = int(input("Enter Amount:- "))
                    
                    if to_usr_id in usr.keys() and usr[to_usr_id].email == to_usr_email:
                        recp = usr[to_usr_id]
                        pass_ = input("Enter Your Password to Confirm transaction:- ")

                        if pass_ == user.passwrd:
                            recp,status = user.transfer(amount=amount, to_id=recp)
                            
                            if status == 1:
                                print("Transaction Successful")
                                #add user to active users
                                usr[user.unique_id] = user
                                usr[recp.unique_id] = recp
                            else:
                                print("Transaction Failed, Insufficient Balance")
                            
                            _ = input('Press any key to continue')
                            continue
                        else:
                            print("Incorrect password")
                            _ = input('Press any key to continue')
                            continue
            else:
                #clear screen
                os.system("reset")

                print('Unique Id or Password Not Correct')
                _ = input('Press any key to continue')
                continue
            # #creare user account
            # user = Bankingapp(Name, Email, Passwrd)

            # #add user to active users
            # usr[user.unique_id] = user

            # #add email to active emails
            # emails.append(user.email)

            # #clear screen
            # os.system("reset")

            # #print user details
            # #clear screen
            # os.system("reset")
            
            # #error message
            # print(f'Account Succesfully Created -- your Unique is is {user.unique_id} remember it for later login\n')
            # _ = input('Press any key to continue')

        else:
            print('Invalid Respnse')
            continue