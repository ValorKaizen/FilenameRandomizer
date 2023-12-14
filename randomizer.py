import os
import random
import string

while True:
    directory = input("Enter directory:")
    print("Editing ", directory)
    check = input("(Y/N)\n")
    if (check.upper() != "Y"):
        exit()
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            name, extension = os.path.splitext(f)
            ran = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            os.rename(name + extension, directory + "\\" + ran + extension)
            print("File randomized as: " + ran + extension)
