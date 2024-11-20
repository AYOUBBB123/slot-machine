# import section
import os
import shutil

print("PART 2: File Handling Operations \n\n")

print("Lesson 1  : Creating Files \n")


print("Exercise 1: \n ")
file = open("scores.txt","w")

file.write("15\n")
file.write("12\n")
file.write("3\n")
file.close()
print("done u crated 'scores.txt' and u wrote the three names \n ")


files = open("students.txt","w")
files.write("john\n")
files.write("Jane fjfop\n")
files.write("ayoub owkf\n")
files.write("mouhmd\n")
files.write("abdou\n")
files.close()

with open("scores.txt","r") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()



print("Exercise 2: \n ")
print("Write a program to print only the first three lines from scores.txt using readlines().\n")

with open("scores.txt","r") as file:
    lines = file.readlines()
    for line in lines[:3]:
        print(line.strip())



print("Exercise 3: \n ")
print(": Add more students to the students.txt file. \n")

with open ("scores.txt","a") as file:
    file.write("5 \n")
    file.write("1 \n")
print("done i add two students to the scores.txt file. \n")




print("Exercise 4: \n ")
print(": Create and delete a temporary file named temp.txt. \n")
temp = open("temp.txt","w")
temp.write("hi")
temp.close()
os.remove("temp.txt")
print("temp.txt deleted successfully")




print("Exercise 5: \n ")
print(": Write a program to copy scores.txt to backup_scores.txt. \n")
print("we imported shutil ")
shutil.copy("scores.txt","backup_scores.txt")
print("\n the backup is done \n")



print("Exercise 6: \n ")
print(": Merge two files classA.txt and classB.txt into all_classes.txt. \n")


print("first creating file class A and B \n")
classA = open("classA.txt","w")
classA.write("this is the classA \n")
classA.close()

print("classA has been created\n")

classB = open("classB.txt","w")
classB.write("this is the classB \n ")
classB.close()

print("classB has been created \n")


with open("all_classes.txt","w") as outFile:
    for files in ["classA.txt","classB.txt"]:
        with open(files) as inFile:
            outFile.write(inFile.read())
print("classes have been merged \n")



print("Exercise 7: \n ")

bigFile = open("theTenLineFile.txt","w")
for i in range(1,11):
    bigFile.write(f"line number {i} \n")
bigFile.close()
print("the theTenLineFile.txt has been written \n")

with open("theTenLineFile.txt","r") as fileTwo:
    lines = fileTwo.readlines()
    with open ("theFirstPart.txt","w") as part1:
        part1.writelines(lines[:5])
    with open ("theSecendPart.txt","w") as part2:
        part2.writelines(lines[5:11])

print("the file has been split \n")

def myFunc(lines):
        while lines:
            return int(lines)

with open("scores.txt","r") as file:
    lines = file.readlines()
    lines.sort(key = myFunc)
with open("sorted.txt","w") as sortedFile:
    sortedFile.writelines(lines)


with open("students.txt", "r") as file:
 for line in file:
    if "Jane" in line:
        print("the line that contain the name ur looking for is : \n",line.strip() )

