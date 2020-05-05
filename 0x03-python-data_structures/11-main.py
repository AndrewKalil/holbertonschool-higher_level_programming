#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
my_list2 = [1, 2, 3, 4, 5]
empty_list = []
idx = 3
idxx = 8
new_list = delete_at(my_list, idx)
new_empty_list = delete_at(empty_list, idx)
new_list_large_idx = delete_at(my_list2, idxx)
print(new_list)
print(my_list)
print("-"*50)
print("if list was to be empty")
print(new_empty_list)
print("if idx was to be larger than list length")
print(new_list_large_idx)
