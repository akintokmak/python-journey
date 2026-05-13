with open("file1.txt", "r") as file1:
    file1_list = [int(num) for num in file1.readlines()]
with open("file2.txt", "r") as file2:
    file2_list = [int(num) for num in file2.readlines()]

result = [num for num in file2_list if num in file1_list]
print(result)