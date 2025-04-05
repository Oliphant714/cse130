import json

filename = input("What is the name of the file? ").lower()
correctfile = False

while not correctfile:
    if not filename.endswith(".json"):
        filename += ".json"
    try:
        with open(f'W11/{filename}', 'rt') as filehandle:
            data = json.load(filehandle)

            assert "array" in data
            assert isinstance(data["array"], list)
            
            correctfile = True
    except (FileExistsError, FileNotFoundError):
        print("File not found.")
        filename = input("What is the name of the file? ").lower()

window_size = int(input("Enter the window size: "))

def highest_average(array, window_size):
    assert window_size > 0, "Window size must be greater than 0"
    assert window_size <= len(array), "Window size must be less than or equal to the length of the array"
    window_sum = sum(array[:window_size])
    max_sum = window_sum

    for i in range(window_size, len(array)):
        window_sum += array[i] - array[i - window_size]
        max_sum = max(max_sum, window_sum)
    return max_sum / window_size

print("The highest average of the list is:", highest_average(data["array"], window_size))