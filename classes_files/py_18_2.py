msg = 'Give Your Carrer a Competitive Edge With Globally Recognized Certifications\n\n'
msgs = ['Python\n', 'Sql\n', 'HTML\n', 'CSS\n', 'JavaScript\n', 'Django\n', 'React\n', 'AWS\n']

f = open("doc_one", 'w')
f.write(msg)
f.writelines(msgs)      # array data printing
f.close()

f = open('doc_one', 'r')
data = f.read()
print(data)
f.close()