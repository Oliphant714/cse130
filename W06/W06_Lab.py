# 1. Name:
#      Isaac Oliphant
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      This program reads a JSON file and sorts the array in the file. It then asks the user for a value to search for in the array. The program uses a binary search to find the value in the array and returns the index of the value if it is found.
# 4. Algorithmic Efficiency
#      My overall efficiency is O(m log m) becuase of the two main operations happening. The first operation is sorting the array which is O(m log m) and the second operation is the binary search which is O(log m). The overall efficiency is O(m log m) because the binary search is the most efficient operation.
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part is and will always be completing the video in under a minute or two, but the hardest part of the program was putting together the binary search with strings rather than integers.  I took the code from previous assignments as to how to implement a JSON file, but I had to change the binary search to work with strings.
# 6. How long did it take for you to complete the assignment?
#      Roughly 2 hours on code and 2 hours reading.

import json

filename = input("What is the name of the file? ").lower()

if not filename.endswith(".json"):
    filename += ".json"

try:
    with open(f'W06\{filename}', 'rt') as filehandle:
        data = json.load(filehandle)
except (FileExistsError, FileNotFoundError):
    print("File not found.")

datalist = data.get("array", [])
datalist.sort()

def search_list(list, value):
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        mid_value = list[middle]
        
        if mid_value == value:
            return middle  
        elif mid_value < value:
            left = middle + 1  
        else:
            right = middle - 1
            
    return -1  

treasure = input("What are you looking for? ").title()
inlist = search_list(datalist, treasure)

if inlist != -1:
    print(f"We found '{treasure}' in {filename}.")
else:
    print(f"Sorry, '{treasure}' is not in {filename}.")