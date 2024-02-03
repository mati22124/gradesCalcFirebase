from grades import grade

#Configure and Connext to Firebase

#Login function

school = grade()

#Main

ans=input("Are you a new user?[y/n]")


if ans == 'n':
    school.login("mayanktiku04@gmail.com", "mati22123")
    print(school.user)
    print("\n\n")
    print(school.data)
    print(str(school.sumPointsHave(0))+" / "+str(school.sumPointsOutOf(0)))
    print(school.getGrade(0))
    school.setInfo()
    print("successfull")
elif ans == 'y':
    email = input("enter your email: ")
    passwd = input("enter your password: ")
    school.signup(email, passwd)
    print(school.user)
    print("\n\n")
    print(school.data)
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