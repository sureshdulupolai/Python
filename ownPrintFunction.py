def my_print(*args, sep=' ', end='\n'):
    output = ''
    for arg in args:
        output += str(arg) + sep
    output = output.rstrip(sep)  # last sep ko hata do
    output += end  # end add karo
    import sys
    sys.stdout.write(output)  # directly terminal pe likho

# Example Usage:
my_print("Hello", "Suresh!", "Welcome", sep=' - ')
my_print()
my_print([1, 2, 3])