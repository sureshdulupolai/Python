# 10, 12,13, start 16
# 1. Print numbers from 1 to 10 using a `while` loop.

count = 1
while count <= 10:
    print(count)
    count = count + 1


# 2. Print all even numbers between 1 and 20.

count = 2
while count <= 20:
    print(count)
    count = count + 2


# 3. Print all odd numbers between 1 and 20.

count = 1
while count <= 20:
    print(count)
    count = count + 2


# 4. Sum all numbers from 1 to 100.

count = 1
total = 0
while count <= 100:
    total += count
    count += 1
print(total)


# 5. Print a multiplication table for the number 7.

count = 1
while count <= 10:
    print(f"7 * {count} = {7 * count}")
    count += 1


# 6. Print the first 10 squares (1², 2², ..., 10²).

count = 1
while count <= 10:
    print(count ** 2)
    count += 1


# 7. Print the factorial of a number (e.g., 5).

num = 5
count = 1
factorial = 1
while count <= num:
    factorial *= count
    count += 1
print(factorial)


# 8. Print the Fibonacci series up to the 10th number.

count = 0
a, b = 0, 1
while count < 10:
    print(a)
    a, b = b, a + b
    count += 1


# 9. Print numbers from 10 down to 1 using a `while` loop.

count = 10
while count >= 1:
    print(count)
    count -= 1


# 10. Check if a number is prime (check if 13 is prime).

num = 13
count = 2
is_prime = True
while count < num:
    if num % count == 0:
        is_prime = False
        break
    count += 1
print(is_prime)


# 11. Print all numbers divisible by 3 between 1 and 30.

count = 3
while count <= 30:
    if count % 3 == 0:
        print(count)
    count += 1


# 12. Calculate the sum of digits of a number (e.g., 123).

num = 123
total = 0
while num > 0:
    total += num % 10
    num //= 10
print(total)

# 13. Check if a number is a palindrome (e.g., 121).

num = 121
original_num = num
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(original_num == reversed_num)


# 14. Print all the numbers divisible by 5 between 1 and 50.

count = 5
while count <= 50:
    if count % 5 == 0:
        print(count)
    count += 5


# 15. Print the first 10 numbers in the pattern 1, 3, 5, 7, ...

count = 1
while count <= 19:
    print(count)
    count += 2


# 16. Reverse a string using a `while` loop (e.g., "hello").

s = "hello"
reversed_str = ""
i = len(s) - 1
while i >= 0:
    reversed_str += s[i]
    i -= 1
print(reversed_str)


# 17. Print the sum of even numbers between 1 and 50.

count = 2
total = 0
while count <= 50:
    total += count
    count += 2
print(total)

# 18. Check if a number is a perfect number (e.g., 28).

num = 28
count = 1
divisors_sum = 0
while count < num:
    if num % count == 0:
        divisors_sum += count
    count += 1
print(divisors_sum == num)


# 19. Count the number of vowels in a string (e.g., "hello").

s = "hello"
vowels = "aeiou"
count = 0
i = 0
while i < len(s):
    if s[i] in vowels:
        count += 1
    i += 1
print(count)


# 20. Print the first 10 numbers that are divisible by 4.

count = 4
while count <= 40:
    print(count)
    count += 4


# 21. Print all multiples of 6 from 1 to 60.

count = 6
while count <= 60:
    print(count)
    count += 6


# 22. Calculate the sum of all numbers from 1 to 50 that are divisible by 3.

count = 3
total = 0
while count <= 50:
    total += count
    count += 3
print(total)


# 23. Print the square root of numbers from 1 to 10.

import math
count = 1
while count <= 10:
    print(math.sqrt(count))
    count += 1


# 24. Print the sum of squares of numbers from 1 to 5.

count = 1
total = 0
while count <= 5:
    total += count ** 2
    count += 1
print(total)


# 25. Print the powers of 2 up to 2^10.

count = 0
while count <= 10:
    print(2 ** count)
    count += 1


# 26. Print all prime numbers less than 50.

num = 2
while num < 50:
    is_prime = True
    count = 2
    while count < num:
        if num % count == 0:
            is_prime = False
            break
        count += 1
    if is_prime:
        print(num)
    num += 1


# 27. Print numbers from 1 to 100 that are divisible by both 3 and 5.

count = 1
while count <= 100:
    if count % 3 == 0 and count % 5 == 0:
        print(count)
    count += 1


# 28. Print numbers between 1 and 50 that are not divisible by 4.

count = 1
while count <= 50:
    if count % 4 != 0:
        print(count)
    count += 1


# 29. Count the number of digits in a number (e.g., 12345).

num = 12345
digit_count = 0
while num > 0:
    digit_count += 1
    num //= 10
print(digit_count)


# 30. Print the number of occurrences of a specific character in a string (e.g., 'l' in "hello")

s = "hello"
char = "l"
count = 0
i = 0
while i < len(s):
    if s[i] == char:
        count += 1
    i += 1
print(count)
