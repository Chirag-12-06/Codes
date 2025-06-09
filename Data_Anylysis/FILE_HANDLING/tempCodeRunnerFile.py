import os

with open('text.txt', 'r') as file:
    content = file.read()  
    print(content)

with open('text.txt', 'r') as file:
    for l in file:
        print(l.strip())



with open('text.txt', 'w') as file:
    file.write('resvsd')

with open('text.txt', 'a') as file:
    file.write('resvsd')

lines=['fe','54','yjuyfbd']
with open('text.txt','a') as file:
    file.writelines(lines)