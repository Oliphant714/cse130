number_list = [41, 45, 47, 32, 49, 40, 32]
window_size = 4

def highest_average(array, window_size):
    window_sum = sum(array[:window_size])
    max_sum = window_sum

    for i in range(window_size, len(array)):
        window_sum += array[i] - array[i - window_size]
        max_sum = max(max_sum, window_sum)
    return max_sum / window_size

print("The highest average of the list is:", highest_average(number_list, window_size))