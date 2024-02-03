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
    
