try: #Using try/except creates a condition for if the code crashes.
    with open("myname.txt", "wt") as filehandle: #Using 'wt' completely destroys and recreates the file.  If I use 'a', it will continue to add to the file.
        filehandle.write("Jimmy Joe")
except (FileExistsError, FileNotFoundError):
    print("File not found")

try:
    with open("myname.txt", "rt") as filehandle:
        name = filehandle.read()
        print(f'Your name is {name}.')
except (FileExistsError, FileNotFoundError):
    print("File not found.")