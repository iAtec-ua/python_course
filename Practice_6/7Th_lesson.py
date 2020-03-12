"""try:
    file = open('test.txt', encoding='utf-8')
    tmp = file.read()
    print(tmp)
finally:
    file.close()"""

with open('test.txt', 'w', encoding='utf-8') as file:
    file.write("first line ")
    file.write("second \n")
    file.writelines("contains two lines \n")

file = open('test.txt', 'r', encoding='utf-8')
print(file.read(5))
print(file.read(5))
print(file.read())
