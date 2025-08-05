# serialization / deserialization of a list

# f.seek(0, 0)      # beginning of the string
# f.seek(12, 0)     # 12 character right from the beginning of the string

import json

f = open('doc_two', 'w+')
lst = [10, 20, 30, 40, 50]
# (lst , fileobject)
json.dump(lst, f)
f.seek(0)       # cursor - in line no one before, curor[10, 20, 30, 40, 50]
lst_data = json.load(f) + [100]     # retriving data of list and printing in terminal and adding value = [100]
print(lst_data)
f.close()


# dict
f = open('doc_two', 'w+')
dict1 = {'A' : 10, 'B' : 20, 'C' : 30}
json.dump(dict1, f)
f.seek(0)
lst_data = json.load(f)
print(lst_data)
f.close()