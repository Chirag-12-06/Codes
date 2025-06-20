import os

with open('text.txt', 'r') as file:
    content = file.read()  
    print(content)

with open('text.txt', 'r') as file:
    for l in file:
        print(l.strip())



with open('text.txt', 'w') as file:
    file.write('replace this text\n')

with open('text.txt', 'a') as file:
    file.write('replace this text\n')

lines=['fe\n','54\n','u\n']
with open('text.txt','a') as file:
    file.writelines(lines)