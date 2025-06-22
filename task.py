def merge_lists_to_dict(keys,values):
    return dict(zip(keys,values))
values = [1,2,3,4]
keys = [5,6,7,8]
result_one = merge_lists_to_dict(keys=keys,values=values)
result_two = merge_lists_to_dict(keys,values=values)
print(result_one)
print(result_two)