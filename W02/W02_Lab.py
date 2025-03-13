import json

try:
    with open('W02\Lab02.json', 'rt') as filehandle:
        data = json.load(filehandle)
except (FileExistsError, FileNotFoundError):
    print("File not found.")

usernames_list = data.get('username')
passwords_list = data.get('password')

usernames_dictionary = {username: password for username, password in zip(usernames_list, passwords_list)}
passwords_dictionary = {password: username for password, username in zip(passwords_list, usernames_list)}

keep_going = "Y"

while keep_going == "Y":
    username = input("Please enter your username:\n")
    password = input("Please enter your password: \n")

    id_name = usernames_dictionary.get(username)

    if id_name is None or id_name != password:
        print("You are not authorized to use this system.")
    else:
        print("You are authorized!")
    keep_going = input("Would you like to continue? Y/N  ").upper()
