students = {}
average = []
while(True):
    sId = input("Enter student id: ")
    n = int(input("Enter number of courses registered: "))
    courses = {}
    s=0
    for i in range(n):
        c = input("Enter course name, ECTS, grade: ")
        coursesList = c.split(",")
        courses[coursesList[0]]=(coursesList[1],coursesList[2])
        s+=int(coursesList[1])
    average.append(s/n);
    students[sId] = courses
    choice = input("Do you want to continue Y/N? ")
    if(choice == 'N'):
        break
    
print(students)
k=0
for key,value in students.items():
    print("Student id:{0} \t G.P.A:{1: .2f}".format(key, average[k]))
    k=k+1