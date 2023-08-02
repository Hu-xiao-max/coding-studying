nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]]
merged_list = [item for sublist in nested_list for item in sublist]
print(merged_list)