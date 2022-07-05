import os
os.remove("myfile.txt")


f1 = open("Sample.txt", "a")
f1.write("Now the file has more content!")
f1.close()
f1 = open("Sample.txt", "r")
print(f1.read())

