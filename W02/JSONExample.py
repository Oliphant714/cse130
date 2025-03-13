import json
my_friend = {
    "Name" : "Jennie",
    "Phone" : "8765309",
    "Address" : "555 Cherry Lane",
    "Email" : "jennielucas@gmail.com"
}

#print(my_friend)

try:
    with open('JsonExample2.json', "wt") as filehandle:
        data_dictionary = json.dumps(my_friend)
        print(data_dictionary)
except (FileExistsError, FileNotFoundError):
    print("File not found.")

with open('JsonExample2.json', "rt") as filehandle:
    # data = filehandle.read()
    # print(data)
    data_dictionary = json.load(filehandle)
    print(data_dictionary['Name'])
    print(data_dictionary['Phone'])