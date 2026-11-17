# So its day three and today topic is :
# FOR LOOP : Imagine you want  write hello ten time without loop your code look like this "prin("hello")".
# But with the loop you can write this instead :

for i in range (1,11):
    print("hello")
 
# Challenge 1. :

for i in range(1,11):
    print(i)
print("python is amazing")

# challenge 2. :
for i in range(2,21,2):
    print(i)
print("All even numbers is completed")

# Challenge 3. :
for i in range (20,0,-1):
    print(i)
print("Countdown is completed")

# Now the second topic "WHILE LOOP":
# While loop excute output untill the condition is true:

# Challenge 1. :

i = 1

while i <= 10:
    print(i)
    i = i + 1

# Challenge 2. :

number = int(input("pls enter a number:"))
i = 1

while i <= 10:
    print(number, "x",i,"=", number * i)
    i = i + 1
    