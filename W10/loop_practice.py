prompt = int(input("Enter a number: "))

# sum = 0
# for i in range(0, prompt + 1):
#     sum += i
#     if i != prompt:
#         print(i, end=" + ")
#     if i == prompt:
#         print(i)
# print(f"The sum of all numbers from 0 to {prompt} is {sum}.")

# base = 2
# for i in range(1, prompt + 1):
#     print(f"{base}^{i} = {base ** i}")

# base = 1
# for i in range(1, prompt + 1):
#     base *= i
#     print(f"{base}")

# base = 1
# count = 1
# while count <= prompt:
#     base *= count
#     count += 1
#     print(f"{base}")

base = 1
numbers_list = list(range(1, prompt + 1))
for i in numbers_list:
    base *= i
    print(base)