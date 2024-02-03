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
2. add class
3. add assignment
5. remove class
6. remove grade
7. calculate grade needed for a _
8. calulate minimum grade needed to keep your current grade.
""")

# data = {
#   "classes": [ #array of classes
#     { #start of first class
#       "name": "class1",
#       "assignments": [ #array of assignments
#         { #start of first assignment
#           "name": "assignment 1",
#           "pointsHave": 2,
#           "pointsOutOf": 2,
#           "Category": "Unweighted",
#           "Weight": 1
#         },
#         { #start of 2nd assignemnt
#           "name": "assignment 2",
#           "pointsHave": 5,
#           "pointsOutOf": 5,
#           "Category": "Unweighted",
#           "Weight": 1 
#         }
#       ]
#     }
#   ]
# }