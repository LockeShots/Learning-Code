#Ask the user for a username and then ask for the password.
#If the username and password are correct give a message approved and exit.
#After 3 incorrect attempts, print denied and exit.
#Extension: delay for 2 seconds on incorrect password

import csv

def filetodatabase(file):
    with open(file, 'r') as f:
        data = csv.reader(f, delimiter ='|')
        credentials = {rows[0]:rows[1] for rows in data}
        return credentials

def appendtodatabase(data, database):
    (database).update((data))

def databasetofile(file,database):
    with open (file, 'w', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        for key, val in database.items():
            writer.writerow([key,val])

def usernamesetter(attempts, database):
    count = 0
    while count <=(attempts):
        username = input(f'Please choose a username: ')
        if (username) in (database):
            count += 1
            print('That username is taken.')
        else:
            count = (attempts)+1
            print('Thank you, your username has been set.')
            return username
    else:
        print('You have run out of attempts, please try again.')
        exit()

def passwordsetter(attempts, database):
    count = 0
    while count <=(attempts):
        password = input('Please choose a password: ')
        password2 = input('Please enter your password again: ')
        if password != password2:
            count += 1
            print ('Your passwords do not match, try again.')
        else:
            count = (attempts)+1
            print ('thank you, your password has been set.')  
            return password
    else:
        print ('Please try again.')
        exit()

def usernameasker(attempts, database):
    count = 0
    while count <=(attempts):
        username = input('Enter Your Username: ')
        if (username) in (database):
            count = (attempts)+1
            return username
            break
        else:
            count += 1
            print("This username doesn't exist, please retry")
    else:
        print("Maximum attempts reached, please run again.")
        exit()

def passwordasker(attempts, database, username):
        count = 0
        while count <=(attempts):
            password = input('Enter Your Password: ')
            if password == (database)[username]:
                count = (attempts)+1
                print('Correct')
                break
            else:
                print('Incorrect password')
                count += 1
        else:
            from time import sleep
            sleep(2)
            print('Denied for being wrong three times (what a muppet!)')
            exit()

def set_credentials():
    username = usernamesetter(2,credentials)
    password = passwordsetter(2,credentials)
    appendtodatabase(({(username):(password)}),credentials)
    databasetofile('training_task_1_-_credentials.csv',credentials)

def request_credentials():
    username = usernameasker(2,credentials)
    passwordasker(2,credentials,username)

if __name__ == '__main__':
    credentials = filetodatabase('training_task_1_-_credentials.csv')
    choice = input('Do you wish to sign up or log in? ')
    if choice == 'sign up':
        set_credentials()
        request_credentials()
    if choice == 'log in':
        request_credentials()
    else:
        print('Please try again and enter either "sign up" or "log in"')
        exit()