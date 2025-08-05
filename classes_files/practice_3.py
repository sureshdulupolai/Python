lst1 = ['suresh', 'aman', 'nitin', 'harsh', 'arpit', 'hemang', 'adarsh', 'pankaj']
lst2 = ['kumar', 'yadav', 'sharma', 'shetty', 'singh', 'rajput', 'vishwakarma', 'gupta']


#  Expected Output:
# {
#     'adarsh gupta': (0, ('adarsh', 'gupta')),
#     'aman yadav': (1, ('aman', 'yadav')),
#     'arpit singh': (2, ('arpit', 'singh')),
#     'harsh shetty': (3, ('harsh', 'shetty')),
#     'hemang rajput': (4, ('hemang', 'rajput')),
#     'nitin sharma': (5, ('nitin', 'sharma')),
#     'pankaj kumar': (6, ('pankaj', 'kumar')),
#     'suresh vishwakarma': (7, ('suresh', 'vishwakarma'))
# }

# -------------------------------------------------

# ### 1. **Full Name Count:**
#    Write a function `count_full_names(lst1, lst2)` that returns the total number of unique full names (first name + last name) formed from the two lists. If the names overlap, consider them only once.


# a2 = list()
# for a1 in range(len(lst1)):
#     a2 += [[lst1[a1] + ' ' + lst2[a1]]]
# # print(a2)
# c1 = list()
# count = 0
# for b1 in a2:
#     for b2 in b1:
#         if b2 in c1:
#             count += 1
#         else:
#             c1 += [b2]  
# if count == 0:
#     print('Not Repated Names Inside List')
# else:
#     print('Yes Repeated Names Inside List')



# ### 2. **Merge with Custom Delimiter:**
#    Write a function `merge_with_delimiter(lst1, lst2, delimiter)` that merges the names in `lst1` and `lst2` into a list of full names, but with a custom delimiter between the first and last names.


# a2 = list()
# for a1 in range(len(lst1)):
#     a2 += [[lst1[a1], lst2[a1]]]
# print(a2)

# ### 3. **Matchmaking:**
#    Write a function `find_matching_pairs(lst1, lst2)` that returns a list of tuples where each tuple contains the first and last name where the first name in `lst1` and the last name in `lst2` have the same length.


# b1 = list()
# for a1 in range(len(lst1)):
#     b2 = list()
#     for a2 in range(len(lst1)):
#         if len(lst1[a1]) == len(lst2[a2]):
#             b2 += [lst1[a1],lst2[a2]]
#     b1 += [b2]
# print(b1)



# ---

# ### 4. **Name Initials:**
#    Write a function `get_initials(lst1, lst2)` that returns a list of initials for each person (first name initial + last name initial).

#    **Function Signature:**
#    ```python
#    def get_initials(lst1: List[str], lst2: List[str]) -> List[str]:
#    ```

# ---

# ### 5. **Reversed Full Name:**
#    Write a function `reverse_full_names(lst1, lst2)` that returns a list where each full name is reversed, i.e., last name first, then first name.

#    **Function Signature:**
#    ```python
#    def reverse_full_names(lst1: List[str], lst2: List[str]) -> List[str]:
#    ```

# ---

# ### 6. **Name Length Comparison:**
#    Write a function `compare_name_lengths(lst1, lst2)` that returns a dictionary where the key is the full name and the value is the difference in length between the first and last name.

#    **Function Signature:**
#    ```python
#    def compare_name_lengths(lst1: List[str], lst2: List[str]) -> Dict[str, int]:
#    ```

# ---

# ### 7. **Common Suffix Names:**
#    Write a function `find_common_suffix(lst1, lst2)` that returns a list of full names where the first and last name share the same suffix of 3 characters.

#    **Function Signature:**
#    ```python
#    def find_common_suffix(lst1: List[str], lst2: List[str]) -> List[str]:
#    ```

# ---

# ### 8. **Full Name Frequency:**
#    Write a function `name_frequency(lst1, lst2)` that returns a dictionary showing how often each full name appears in the list (even if they only appear once).

#    **Function Signature:**
#    ```python
#    def name_frequency(lst1: List[str], lst2: List[str]) -> Dict[str, int]:
#    ```

# ---

# ### 9. **Shortest Full Name:**
#    Write a function `shortest_full_name(lst1, lst2)` that returns the shortest full name formed by combining elements from `lst1` and `lst2`.

#    **Function Signature:**
#    ```python
#    def shortest_full_name(lst1: List[str], lst2: List[str]) -> str:
#    ```

# ---

# ### 10. **Swap First and Last Names:**
#    Write a function `swap_names(lst1, lst2)` that swaps the first and last names in each pair and returns the list of swapped full names.

#    **Function Signature:**
#    ```python
#    def swap_names(lst1: List[str], lst2: List[str]) -> List[str]:
#    ```

# ---

# ### 11. **First Letter of Last Names:**
#    Write a function `first_letter_last_names(lst1, lst2)` that returns a dictionary where the key is the first letter of the last name, and the value is a list of people with that starting letter in their last name.

#    **Function Signature:**
#    ```python
#    def first_letter_last_names(lst1: List[str], lst2: List[str]) -> Dict[str, List[str]]:
#    ```

# ---

# ### 12. **Full Names With Prefix:**
#    Write a function `add_prefix_to_names(lst1, lst2, prefix)` that adds a given prefix to both the first and last name for each person in the list.

#    **Function Signature:**
#    ```python
#    def add_prefix_to_names(lst1: List[str], lst2: List[str], prefix: str) -> List[str]:
#    ```

# ---

# ### 13. **Alphabetical Last Names:**
#    Write a function `alphabetical_last_names(lst1, lst2)` that returns a list of full names sorted alphabetically by last name.

#    **Function Signature:**
#    ```python
#    def alphabetical_last_names(lst1: List[str], lst2: List[str]) -> List[str]:
#    ```

# ---

# ### 14. **Extract First Names Starting With A:**
#    Write a function `filter_first_names(lst1, lst2)` that returns a list of full names where the first name starts with the letter "A".

#    **Function Signature:**
#    ```python
#    def filter_first_names(lst1: List[str], lst2: List[str]) -> List[str]:
#    ```

# ---

# ### 15. **Name Pair Matching:**
#    Write a function `pair_names_with_conditions(lst1, lst2)` that returns a list of pairs (first name, last name) where the sum of the lengths of the first name and the last name is greater than 10.

#    **Function Signature:**
#    ```python
#    def pair_names_with_conditions(lst1: List[str], lst2: List[str]) -> List[Tuple[str, str]]:
#    ```

# ---

# ### 16. **Create Full Name List From Prefix:**
#    Write a function `create_full_names_from_prefix(lst1, lst2, prefix)` that creates a list of full names where each name starts with a given prefix.

#    **Function Signature:**
#    ```python
#    def create_full_names_from_prefix(lst1: List[str], lst2: List[str], prefix: str) -> List[str]:
#    ```

# ---

# ### 17. **Identify Name Pairs With Same Starting Letter:**
#    Write a function `find_pairs_with_same_starting_letter(lst1, lst2)` that returns a list of tuples containing first and last names that start with the same letter.

#    **Function Signature:**
#    ```python
#    def find_pairs_with_same_starting_letter(lst1: List[str], lst2: List[str]) -> List[Tuple[str, str]]:
#    ```

# ---

# ### 18. **Count Names With Specific Length:**
#    Write a function `count_names_with_length(lst1, lst2, length)` that returns the number of full names where the combined length of the first and last names is exactly equal to a given length.

#    **Function Signature:**
#    ```python
#    def count_names_with_length(lst1: List[str], lst2: List[str], length: int) -> int:
#    ```

# ---

# ### 19. **Find Full Names By Last Name:**
#    Write a function `find_full_names_by_last_name(lst1, lst2, last_name)` that returns a list of full names where the last name matches the input `last_name`.

#    **Function Signature:**
#    ```python
#    def find_full_names_by_last_name(lst1: List[str], lst2: List[str], last_name: str) -> List[str]:
#    ```

# ---

# ### 20. **Create Usernames:**
#    Write a function `generate_usernames(lst1, lst2)` that generates usernames by combining the first name and the last name with a period in between. If the name already exists, append a number to it.

#    **Function Signature:**
#    ```python
#    def generate_usernames(lst1: List[str], lst2: List[str]) -> List[str]:
   
# -----------------------------------------------------------------------------------------

# ### 1. **Full Name Sorting by Length:**
#    Write a function that returns a list of full names (first name + last name) sorted by the total length of the name (first name + last name).


# b1 = []
# for a1 in range(len(lst1)):
#     b1 += [lst1[a1] + lst2[a1]]
# print(b1)
# for i in range(len(b1)):
#     for j in range(len(b1) - 1):
#         # Compare adjacent strings and swap them if they are in the wrong order
#         if b1[j] > b1[j + 1]:
#             b1[j], b1[j + 1] = b1[j + 1], b1[j]
# print(b1)



# ### 2. **Count Names With Same Initial:**
#    Write a function that returns the count of full names where the first name and the last name start with the same letter.


# z2 = []
# for z1 in range(len(lst1)):
#     z2 += [[lst1[z1],lst2[z1]]]
# print(z2)
# count = 0
# for d1 in z2:
#     if d1[0][0] == d1[1][0]:
#         count += 1
#     else:
#         pass
# print(count)



# ### 3. **Check for Duplicate Names:**
#    Write a function that checks if there are any duplicate full names in the lists. If duplicates exist, return a list of those names.


# count = 0
# a1 = []
# for a2 in range(len(lst1)):
#     a1 += [[lst1[a2] + ' ' + lst2[a2]]]
# print(a1)
# d1 = []; d4 = []
# for d2 in a1:
#     for d3 in d2:
#         if d3 in d1:
#             count += 1
#             d4.append(d3)
#             pass
#         else:
#             d1.append(d3)
# print('There are "{}" Name Was Repated Again'.format(count))
# print('Name Repate Again : {}'.format(d4))



# ### 4. **Filter Names by Prefix:**
#    Write a function that returns a list of full names where either the first name or last name starts with a specific prefix (e.g., "ha").


# a1 = []; x1 = 'ha'; x2 = len(x1); d2 = []
# for a2 in range(len(lst1)):
#     a1 += [[lst1[a2], lst2[a2]]]
# for b1 in a1:
#     for b2 in b1:
#         if x1 in b2:
#             d2 += [b2]
# for y1 in d2:
#     if y1[:x2] == x1:
#         print(y1)
    

# ### 5. **Create Full Names With Middle Initial:**
#    Write a function that generates full names by adding a middle initial (e.g., "A") between the first name and last name.


# import random
# a2 = list()
# for a1 in range(len(lst1)):
#     v1 = random.randint(97, 122)
#     a2 += [[lst1[a1] + ' ' + chr(v1) + ' ' +lst2[a1]]]
# print(a2)


# ### 6. **Full Names Starting with a Vowel:**
#    Write a function that returns a list of full names where the first name starts with a vowel (A, E, I, O, U).


# a2 = list(); c1 = []
# for a1 in range(len(lst1)):
#     a2 += [[lst1[a1] + ' ' + lst2[a1]]]
# for b1 in a2:
#     for b2 in b1:
#         b3 = b2.lower()
#         print(b3)
#         if b3[0] in 'aeiou':
#             c1 += [b3]
#         else:
#             continue
# print(c1)
        

# ### 7. **Find Longest Full Name:**
#    Write a function that returns the longest full name (first + last name combined).


# a2 = list()
# for a1 in range(len(lst1)):
#     a2 += [[lst1[a1] + lst2[a1]]]
# c1 = a2[0][0]
# for b1 in a2:
#     for b2 in b1:
#         if len(c1) < len(b2):
#             c1 = b2
#         else:
#             continue
# print(c1)


# ### 8. **Count Full Names with More Than 10 Characters:**
#    Write a function that returns the number of full names (first + last name) that have more than 10 characters.


# a2 = list(); c1= list()
# for a1 in range(len(lst1)):
#     a2 += [[lst1[a1] + lst2[a1]]]
# for b1 in a2:
#     for b2 in b1:
#         if len(b2) > 10:
#             c1 += [b2]
#         else:
#             continue
# print(c1)


# ### 9. **Find Names with Specific Suffix:**
#    Write a function that returns a list of full names where the first name or last name ends with a specific suffix (e.g., "sh").


# a2 = list(); c1 = []
# for a1 in range(len(lst1)):
#     a2 += [[lst1[a1], lst2[a1]]]
# for b1 in a2:
#     for b2 in b1:
#         c2 = []
#         b3 = len(b2) - 3
#         if 'sh' in b2[b3:]:
#             c2 += [b1]
#         c1 += [c2]
# e = list()
# for d1 in c1:
#     if len(d1) > 0:
#         e += [*d1]
# print(e)


# ### 10. **Generate Full Name Length Dictionary:**
#    Write a function that generates a dictionary where the keys are full names (first + last), and the values are the length of each full name.


# --> Pending With Dictonary ________________________________________-------------------------------------


# ### 11. **Generate Email Addresses:**
#    Write a function that generates email addresses for each person by concatenating the first name, last name, and a fixed domain (e.g., `example.com`).


# a2 = list()
# for a1 in range(len(lst1)):
#     a2 += [[lst1[a1]+lst2[a1]+'@gmail.com']]
# print(a2)


# ### 12. **Pair Names with Random Number:**
#    Write a function that pairs the first name and last name, then appends a random number between 1 and 100 to each pair.


# import random
# a2 = list()
# for a1 in range(len(lst1)):
#     a3 = random.randint(1, 100)
#     a2 += [[lst1[a1] + ' ' + lst2[a1],a3]]
# print(a2)


# ### 13. **Create List of Name Pairs with Reverse:**
#    Write a function that returns a list of tuples, where each tuple contains a pair of first and last names, along with their reverse order (last name first, first name second).


# a2 = list()
# for a1 in range(len(lst1)):
#     a3 = tuple()
#     for a5 in range(0, 1):
#         a3 += ((lst1[a1] + ' ' + lst2[a1]), (lst2[a1] + ' ' + lst1[a1]))
#     a2 += [a3]
# print(a2)

    
# ### 14. **Create Usernames with First and Last Initial:**
#    Write a function that creates usernames using the first initial of the first name and the first initial of the last name.


# a2 = list()
# for a1 in range(len(lst1)):
#     a2 += [[lst1[a1][0] + lst2[a1][0]]]
# print(a2)


# ### 15. **Find Names Starting and Ending with Same Letter:**
#    Write a function that returns a list of full names where both the first name and last name start and end with the same letter.


# a2 = list()
# for a1 in range(len(lst1)):
#     if lst1[a1][0] == lst2[a1][len(lst2[a1]) - 1]:
#         a2 += [lst1[a1] + ' ' + lst2[a1]]
#     else:
#         continue
# print(a2)


# ### 16. **Find Full Names Containing Specific Word:**
#    Write a function that returns a list of full names that contain a specific word in either the first or last name (e.g., "man").


# a2 = list()
# for a1 in range(len(lst1)):
#     if 'man' in (lst1[a1] + lst2[a1]):
#         a2 += [lst1[a1] + ' ' + lst2[a1]]
#     else:
#         continue
# print(a2)


# ### 17. **Count Full Names with First and Last Name Length Difference:**
#    Write a function that counts how many full names have a length difference greater than 2 between the first and last name.


# a2 = list(); c1 = []
# for a1 in range(len(lst1)):
#     a2 += [len(lst1[a1]) - len(lst2[a1])]
# for b1 in a2:
#     if b1 < 0:
#         c1 += [abs(b1)]
#     else:
#         c1 += [b1]
# print(c1)


# ### 18. **Generate Full Names for List of Nicknames:**
#    Write a function that combines a list of nicknames with a list of last names to generate full names.


# a2 = []
# for a1 in range(len(lst1)):
#     a2 += [lst1[a1] + ' ' + lst2[a1]]
# print(a2)

# ### 19. **Find Names with Odd Number of Characters:**
#    Write a function that returns a list of full names where the combined length of the first and last name is an odd number.


# a2 = list()
# for a1 in range(len(lst1)):
#     if (len(lst1[a1] + lst2[a1])) % 2 != 0:
#         a2 += [lst1[a1] + lst2[a1]]
# print(a2)


# ### 20. **Combine Names with Separator:**
#    Write a function that takes a separator (e.g., comma, dash, etc.) and combines the first and last names with this separator.


# a2 = list()
# for a1 in range(len(lst1)):
#     a2 += [lst1[a1] + '-' + lst2[a1]]
# print(a2)


# --------------------------------------------------------------------------------------------