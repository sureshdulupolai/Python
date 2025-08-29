lst = ["krishpolai@gmail.com", "akashsahu@gmail.com", "pritam@gmail.com", "ashish@gmail.com",
"kunal121@gmai.com","kalim_234@gmail.com","pankajyadav12@gmail.com","arnav_67@gmail.com"]

# s = input("Enter a Starting Alphabet of Gmail to Check Information : ").lower();e,f = 1,0
# while f < len(lst):
#     a = lst[f]; b = a.split("@"); c = b[0]
#     if c[0] == s:
#         print(e,"-",c[0],"-",lst[f]);e += 1
#     f += 1

# g = input("Enter a Last Value to find : ").lower();f = 0;h = 1
# while f < len(lst):
#     a = lst[f]; b = a.split("@"); c = b[0]; d = len(c) - 1
#     if c[d]== g:
#         print(h,"-",c[d],"-",lst[f]); h += 1
#     f += 1

for i in (1,6):
    print(lst[:i],"\nThis is the len of lst Now : {}".format(len(lst)))

# for i in enumerate(lst):
#     print(i)

# print()
# for i in lst:
#     print(i)