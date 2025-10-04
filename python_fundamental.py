"""
print("I am learning cybersecurity") #STRING
print(10) #Integer
print(-10) #Integer
print(10.0) #Float
print(10.20) #Float
print(True) #Boolean

#VARIABLE

name = "Favour"
course = "Cybersecurity"
regno = 10
score = 60.8

print("Name:", name)
print("Course of Study:", course)
print("Registration No:", regno)
print("Total Score:", score)

#INPUT VARIABLE

name = input("What is your name \t")
course = input("What is your Course of Study\t")
reg = input("What is your Registration Number\t")
score = input("What is your score\t")

print("Name:", name)
print("Course of Study:", course)
print("Registration No:", reg)
print("Total Score:", score)

#CONDTIONAL STATEMENT

score = int(input("Enter your score:"))
if score > 100:
    print("Invalid: Enter a score within the range of 1-100")
if score >= 60 and score <= 100:
    print("Congratulation: You have a distinction")
elif score >=40 and score < 60:
    print("You have Credit")
elif score >=20 and score < 40:
    print("You have a pass")
elif score < 20:
    print("You failed")
else:
    print("Enter a valid score range")
    
"""

#LOOP
"""
for i in range(1,20,2):
    print(i)


no = 20
while no == 20:
    print("You have gain an admission to study cybersecurity")
"""
#FILE HANDLING
"""
#How to open and read from a file
file = open("example.txt","r")
content = file.read()
print(content)
file.close()
"""
"""
file = open("example.txt","r")
for content in file:
    read = content.strip
file.close()


with open("example.txt","r")as file:
    content = file.readline()
    print(content)
    file.close()


#file = open("newfile.txt","w")
#content = file.write("Cybersecrity is a great course\n")
#file.close()

with open("newfile.txt","r")as file:
    content = file.read()
    print(content)
"""

with open("newfile.txt","r+")as file:
    content = file.write("Web development is also a great course\n")
    content = file.read()
    print(content)
    file.close()
    

    
    
    
    
    
    
    
    
    
    
    