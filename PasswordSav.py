import csv

num = 2

while num != 1:
    a = raw_input("Do you want to add or read a password. Can also type quit(please type in read, add or quit): ")
    decision = a.strip()# taking in the user input typed in the command line
    if 'add' in decision or 'Add' in decision:# as long as the words "add" or "Add" are typed, the program assumes it wants to add a password
        website = raw_input("Enter the website for the password: ")
        username = raw_input("Enter the username: ")
        password = raw_input("Enter the password: ")
        print "\nwebsite: ", website
        print "username: ", username
        print "password: ", password, "\n"

        with open ('Passwords.txt', 'a') as curr_file:  # opening the file for appending to add the website name, username and password
            curr_file.write(website)
            curr_file.write('\n')
            curr_file.write("username: ")
            curr_file.write(username)
            curr_file.write('\t')
            curr_file.write("password: ")
            curr_file.write(password)
            curr_file.write('\n\n')

    elif 'read' in decision or 'Read' in decision:  # as long as the words "read" or "Read" are typed, the program assumes it wants to read a password
        array = []
        i = 0
        with open('Passwords.txt', 'r') as curr_file:
            reading = curr_file.readlines()
            array = reading
        ans = raw_input("Do you want to see all the passowrds(yes or no): ")

        if 'yes' in ans or 'Yes' in ans:
            while i < len(array):   # printing all the passwords in the text file if the the user desires
                print(array[i])
                i = i+1

        elif 'no' in ans or 'No' in ans:
            site = raw_input("Enter the website of the password desire:")
            while i < len(array):
                if site == array[i].strip():    # finding the desired username and password for the website specified
                    desiredPassword = array[i+1]    # since the website name is one index before the username and password, must add 1 to i
                    break
                elif i == len(array)-1: # if i reaches the end of the array, meaning no password for the website desired
                    desiredPassword = "No such information regarding desired website, please try again\n"
                    break
                i = i + 1

            print "\n", desiredPassword

    elif decision == 'quit' or decision == 'Quit':  # gave an option to quit when the user is satisfied with their password search
        num = 1
        curr_file.close()
