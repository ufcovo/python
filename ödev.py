studentRecord = dict()   # the main dictionary that records all data
while True :
   stuID = int(input("Enter student id : "))   # get student ID
   subjects = dict()   # create the send dictionary for the subjects
   n = int(input("Enter number of courses registered : "))   # read the number of subjects
   while n > 0 :
       sub = input("Enter course name, ECTS, grade : ")   # get input for each subject
       n -= 1
       data = sub.split(',')   # split the input based on coma(,) symbol
       data[1] = float(data[1])   # convert the second field i.e. marks in to number
       subjects[data[0].strip()] = (data[1], data[2].strip())   # create a tuple for the marks and grade of the subject
   studentRecord[stuID] = subjects;   # add this second dict to the first dict
   ch = input("Do you want to continue Y/N? ")   # ask for continuing
   if ch == 'N':
       break
   elif ch == 'Y':
       continue
print('\n')

honorList = list()   # store the list of Honor students
for student in studentRecord :   # traverse for all students
   print("Student id :", student, "\t GPA: ", end='')  
   marks=0
   for record in studentRecord[student] :   # traverse through all subjects for a particular student
       marks += studentRecord[student][record][0]   # calculate the total marks
   print(marks/len(studentRecord[student]))   # calculate GPA
   if marks/len(studentRecord[student]) >= 3.0 :   # check if Honor student
       honorList.append(student)

print("\nHonor Students with GPA above 3.0")
for student in honorList :       # print Honor student list
   print(student)