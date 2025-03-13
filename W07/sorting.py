num_list = [10, 7, 3, 2, 6, 4, 1, 9, 8, 5]

fruit_list = ["lemon", "apple", "banana", "grape", "orange", "kiwi", "strawberry", "blueberry", "raspberry", "blackberry"]

def sort_list(list):
    list_length = len(list)
    for i in range(list_length-1):
        for j in range(list_length-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

print(sort_list(num_list))

print(sort_list(fruit_list))