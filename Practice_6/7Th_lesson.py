# Open file for reading
"""try:
    file = open('test.txt', encoding='utf-8')
    tmp = file.read()
    print(tmp)
finally:
    file.close()

# Open file for writing
with open('test.txt', 'w', encoding='utf-8') as file:
    file.write("first line ")
    file.write("second \n")
    # Writes lists into file
    file.writelines("contains two lines \n")

# Open file for reading
file = open('test.txt', 'r', encoding='utf-8')
# Read 5 first symbols
print(file.read(5))
# Moves cursor to () position
file.seek(0)
print(file.read(5))
# Tells the position of cursor
print(file.tell())
print(file.read())
print(file.tell())

file.seek(3)
print(file.readline())

print(file.tell())

print(file.seek(0))

# Allows creating a temporary holder for an object
import pickle
t1 = [1, 2, 3]
s = pickle.dumps(t1)
# pickle.dump(s, 'test.txt')
print(s)
t2 = pickle.loads(s)
print(t2)
print(t1 == t2)
print(t1 is t2)

# Shows the location of the current folder
import os

path = os.getcwd()
print(path)

path_b = os.getcwdb()
print(path_b)

# Shows a list of files which are in use
files = os.listdir()
print(files)

# Shows a list of files in a given directory
documents = os.listdir('/Users/Alex/PycharmProjects')
print(documents)

# Allows creating of new directories
import os

os.mkdir('test')
print(os.listdir())

# Allows renaming directories
os.rename('test', 'new_one')
print(os.listdir())


import os

print(os.listdir())
# Allows deleting files
os.remove('test.txt')
print(os.listdir())
# Allows deleting directories if they are empty
os.rmdir('new_one')
print(os.listdir())

# Allows deleting directories if they are not empty
import shutil

shutil.rmtree('new_one')

# Handling exceptions
with open("test.txt", "w+") as file:
    try:
        file.write("Hello World")
    except IOError as exception:
        print("Error with IO")
        print(exception)
    except Exception as exception:
        print("Something is wrong")
        print(exception)"""


# Creating new exceptions
class ValueTooSmallError(Exception):
    pass


class ValueTooLargeError(Exception):
    pass


number = 10
while True:
    try:
        i_numm = int(input("Enter a number: "))
        if i_numm < number:
            raise ValueTooSmallError
        elif i_numm > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Number is small")
    except  ValueTooLargeError:
        print("Number is large")
    except Exception:
        print("Not a number")
