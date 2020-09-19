#Ask the user for a username and then ask for the password.
#If the username and password are correct give a message approved and exit.
#After 3 incorrect attempts, print denied and exit.
#Extension: delay for 2 seconds on incorrect password

def password_request():
    count = 0
    while count < 3:
        username = input('Enter Your Username: ')
        if username == 'Allan':
            password = input('Enter Your Password: ')
        else:
            print('wrong username')
        if username == 'Allan' and password == 'butt':
            print('Correct')
            break
        else:
            print('Incorrect')
            count += 1
    else:
        from time import sleep
        sleep(2)
        print('Denied for being wrong three times (what a muppet!)')

password_request()