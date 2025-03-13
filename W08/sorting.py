# 1. Name:
#      Isaac Oliphant
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      The program allows the user to select a JSON file containing a list and sorts the list using the bubble sort method.  It then displays the sorted list and asks if the user wants to sort another file.  
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out how the asserts were supposed to work.  I already had a few 'if' statements that I thought were doing the job, but I didn't understand that the asserts would end the code if they fired.
# 5. How long did it take for you to complete the assignment?
#      4 hours


import json

def sort_list(lst):
    assert isinstance(lst, list)
    list_length = len(lst)
    for i in range(list_length - 1):
        for j in range(list_length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    assert lst == sorted(lst)
    return lst

keep_going = "y"

while keep_going == "y":
    filename = input("What is the name of the file? ").lower()
    correctfile = False

    while not correctfile:
        if not filename.endswith(".json"):
            filename += ".json"
        try:
            with open(f'W08\Lab08.{filename}', 'rt') as filehandle:
                data = json.load(filehandle)

                assert "array" in data
                assert isinstance(data["array"], list)
                
                correctfile = True
        except (FileExistsError, FileNotFoundError):
            print("File not found.")
            filename = input("What is the name of the file? ").lower()

    sorted_list = sort_list(data["array"])
    
    print(f"The values in {filename} are:")
    for i in sorted_list:
        print(f"    {i}")

    keep_going = input("Would you like to sort another list? (y/n) ").lower()
    
    assert keep_going in ["y", "n"], "Invalid input! Please enter 'y' or 'n'."
