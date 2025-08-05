# -----------------------------------------------------------------
# file handiling

msgOne = "This is Line 1\n"
msgTwo = "This is Line 2\n"

# w+ = read + write
# w = only write
f = open("Message", 'w+')           # create new txt. file 
# you need to do any where then c:/filename to save
f.write(msgOne) # only string goes
f.write(msgTwo)
f.read()
f.close()

# r = only read
f = open('message', 'r')
data = f.read()
print(data)
f.close()
