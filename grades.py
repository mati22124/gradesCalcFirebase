import pyrebase
import json

class grade:
    firebaseConfig = json.load(open("C:/Users/mayan/coding/gradesCalc/gradesCalcFirebase/firebase.json", "r"))
    def __init__(self):
        self.firebase=pyrebase.initialize_app(self.firebaseConfig)
        self.auth=self.firebase.auth()
        self.database = self.firebase.database()

    def login(self, email, password):
        try:
            self.user = self.auth.sign_in_with_email_and_password(email, password)
            print("Successfully logged in!")
       # email = auth.get_account_info(login['idToken'])['users'][0]['email']p0
       # print(email)
            self.data = self.database.child("users/"+self.user['localId']).get(self.user['idToken']).val()["classes"]
            return 0
        except TypeError:
            self.data = []
            return 0
        except:
            print("Invalid email or password")
            return 1
    
    def signup(self, email, password):
        try:
            self.auth.create_user_with_email_and_password(email, password)
            x = self.login(email, password)
            return x
        except: 
            print("Email already exists")
    
    def setInfo(self):
        try:
            x = {"classes": self.data}
            self.database.child("users/"+self.user['localId']).set(x, self.user['idToken'])
        except:
            print("Not signed in or auth not working.")
    
    def addClass(self, name, assignments = list()):
        classs = {
            "assignments": assignments,
            "name": name
        }
        self.data.append(classs)
    
    def addAssignment(self, classId, name = "Untitled", pointsHave = 0, pointsOutOf = 0, Category = "Unweighted", weight = 1):
        assignm = { 
           "name": name,
           "pointsHave": pointsHave,
           "pointsOutOf": pointsOutOf,
           "category": Category,
           "weight": weight
        }
        try:
            self.data[classId]["assignments"].append(assignm)
        except KeyError:
            self.data[classId]["assignments"] = [assignm]
        except:
            print("error smth happened wrong")

    def getClasses(self, withGrade = False):
        x = 0
        for i in self.data:
            if withGrade:
                print(str(x)+": "+i["name"]+" - "+str(self.getGrade(x))+" - "+self.getLetterGrade(x))
            else:
                print(str(x)+": "+i["name"])
            x+=1

    def getAssignments(self, classId):
        x = 0
        for i in self.data[classId]["assignments"]:
            print(str(x)+": "+i["name"]+" - "+str(i["pointsHave"])+"/"+str(i["pointsOutOf"]) + " - " + str(i["pointsHave"]*100/i["pointsOutOf"])+"%") #add 0 handling later
            x+=1

    def sumPointsHave(self, classId):
        sum = 0
        for i in self.data[classId]["assignments"]:
            sum+=(i["pointsHave"] * i["weight"])
        return sum

    def sumPointsOutOf(self, classId):
        sum = 0
        for i in self.data[classId]["assignments"]:
            sum+=(i["pointsOutOf"] * i["weight"])
        return sum
    
    def getGrade(self, classId):
        if self.sumPointsOutOf(classId) != 0:
            return round(self.sumPointsHave(classId)/self.sumPointsOutOf(classId)*100,2)
        else:
            return 0
    
    def getLetterGrade(self, classId):
        x = self.getGrade(classId)
        if x>=93:
            return "A"
        elif x>=90:
            return "A-"
        elif x>=87:
            return "B+"
        elif x>=83:
            return "B"
        elif x>=80:
            return "B-"
        elif x>=77:
            return "C+"
        elif x>=73:
            return "C"
        elif x>=70:
            return "C-"
        elif x>=67:
            return "D+"
        elif x>=63:
            return "D"
        elif x>=60:
            return "D-"
        else:
            return "F"

    def removeClass(self, classId):
        x = self.data.pop(classId)
        print("Would you like to remove "+ x["name"]+ "from your gradebook? (y/n)")
        y = input()
        if y != "y":
            self.data.append(x)
            print("ok, item not removed.")
        else:
            print("done")
    
    def removeAssignment(self, classId, assignmentId):
        x = self.data[classId]["assignments"].pop(assignmentId)
        print("Would you like to remove \""+ x["name"]+ "\" from your gradebook? (y/n)")
        y = input()
        if y != "y":
            self.data[classId]["assignments"].append(x)
            print("ok, item not removed.")
        else:
            print("done")