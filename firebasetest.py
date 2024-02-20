from grades import grade

#Configure and Connext to Firebase

#Login function

school = grade()

#Main
print("""
1. Login
2. Signup
""")

ans=input("Enter your choice here: ")
while True:
    if ans == '1':
        email = input("enter your email: ")
        passwd = input("enter your password: ")
        x = school.login(email, passwd)
        if x==0:
            break
    elif ans == '2':
        email = input("enter your email: ")
        passwd = input("enter your password: ")
        x = school.signup(email, passwd)
        if x==0:
            break


print("""
1. print classes w/ grade
2. print classes w/o grade
3. print assignments for a certain class
4. add class
5. add assignment
6. remove class
7. remove assignment
8. calculate grade needed for a _
9. calulate minimum grade needed to keep your current grade.
0. save and exit

enter your choice here (number): 
""")


while True:
    x = input()
    if x == "0":
        school.setInfo()
        print("information saved. thanks for using")
        break
    if x == "1":
        school.getClasses(True)
    if x == "2":
        school.getClasses()
    if x == "3":
        school.getClasses()
        y = int(input("what is the class number? "))
        school.getAssignments(y)
    if x == "4":
        name = input("Enter the class name: ")
        school.addClass(name)
    if x == "5":
        school.getClasses()
        y = int(input("what is the class number? "))
        name = input("Assignment name: ")
        poo = int(input("How many points is it out of: "))
        ph = int(input("How many points did you get: "))
        school.addAssignment(y, name, ph, poo)
    if x == "6":
        y = int(input("what is the class number? "))
        school.removeClass(y)
    if x == "7":
        school.getClasses()
        y = int(input("what is the class number? "))
        school.getAssignments(y)
        z = int(input("what is the assignment number? "))
        school.removeAssignment(y, z)