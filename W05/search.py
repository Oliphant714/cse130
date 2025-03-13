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

list = (6, 17, 23, 26, 28, 30, 31, 32, 35, 41, 44, 47, 48, 61, 68, 82, 88, 93, 96, 98)

value = int(input("Enter an integer: "))

position = search_list(list, value)
if position > -1:
    print(f"The value was found at {position}")
else:
    print("Your value is not in the list.")