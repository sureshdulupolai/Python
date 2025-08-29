"""
1. 
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print()

"""
2. 
*
* *
* * *
* * * *
* * * * *
"""

for i in range(0,6):
    for j in range(0,i):
        print("*", end=" ")
    print()

# or
print()

r = 5
for i in range(1, r+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

"""
3.
* * * * *
* * * *
* * * 
* *
*
"""
print()
for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

"""
4.
1
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
print()
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

"""
5. 
5 4 3 2 1
4 3 2 1 
3 2 1 
2 1 
1
"""
print()
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

"""
6. 
    *
   * *
  * * *
 * * * *
* * * * *
"""
