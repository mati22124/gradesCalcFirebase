x = int(input("enter 1 for points, 2 for % weighted: "))

if x == 1:
    print("Enter the point values of right side here. type done when finished.")
    total = 0
    y = input()
    while y.upper() != "DONE":
        total+=float(y)
        y = input()
    print("Total amount of points in gradebook: "+str(total))
    print("Enter the grade you have in the class. MUST BE TO 2 DECIMAL PLACES")
    currentGrade = float(input())
    # work on accuracy l8r
    points = round(currentGrade*total/100, 2)
    print("total points you have: " + str(points))

while True:
    x = int(input(("What would you like to do:\n0. exit\n1. calc min possible letter grade possible\n2. calc grade needed to reach a certain grade\n\n")))
    if x == 0:
        print("thanks for using.")
        break
    if x == 1:
        y = float(input("how many points left to go in the gradebook: "))
        print("if you get 100% of these points, you will end with a "+str(round(((points+y)/(total+y))*100, 2)))
        z = float(input("what percent did you think you will get: "))
        z/=100.0
        print("if you get " + str(z*100) + "% of these points, you will end with a "+str(round(((points+(y*z))/(total+y))*100, 2)))
    