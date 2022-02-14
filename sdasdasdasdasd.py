student_info = {} #holds student information

def info_of_grade (student_info, j):
	if student_info [stu] [j] [1] == "AA" or student_info [stu] [j] [1] == "aa":	#This is for who takes the note 'AA'
		return 4
	if student_info [stu] [j] [1] == "BA" or student_info [stu] [j] [1] == "ba":	#This is for who takes the note 'BA'
		return 3.5
	if student_info [stu] [j] [1] == "BB" or student_info [stu] [j] [1] == "bb":	#This is for who takes the note 'BB'
		return 3
	if student_info [stu] [j] [1] == "CB" or student_info [stu] [j] [1] == "cb":	#This is for who takes the note 'CB'
		return 2.5
	if student_info [stu] [j] [1] == "CC" or student_info [stu] [j] [1] == "cc":	#This is for who takes the note 'CC'
		return 2
	if student_info [stu] [j] [1] == "DC" or student_info [stu] [j] [1] == "dc":	#This is for who takes the note 'DC'
		return 1.5
	if student_info [stu] [j] [1] == "DD" or student_info [stu] [j] [1] == "dd":	#This is for who takes the note 'DD'
		return 1	
	if student_info [stu] [j] [1] == "FD" or student_info [stu] [j] [1] == "fd":	#This is for who takes the note 'FD'
		return 0.5
	if student_info [stu] [j] [1] == "FF" or student_info [stu] [j] [1] == "ff":	#This is for who takes the note 'FF'
		return 0	

while (True):
	stu_num = int (input ("Enter student number: ")) # Take the student id
	courses = dict ()  # create the send dictionary for the courses
	number_of_courses = int (input ("Enter the number of courses registered: ")) # Take the number of courses
 
	for i in range (number_of_courses):
		course_info = input ("Enter course name, ECTS, grade: ")  # Take the course name, ECTS and grade
		stu_cou_info = course_info.split (',') # split the input based on coma(,) symbol
		stu_cou_info[1] = float (stu_cou_info [1]) #converting ECTS in to number
		courses [stu_cou_info [0].strip()] = (stu_cou_info [1], stu_cou_info [2].strip()) #creating a tuple for the marks and grades
	
	student_info [stu_num] = courses	# To add this second dict to the first dict

	check = input ("Do you want to continue Y/N?: ")	# To ask and check for continuing
	if(check == 'N' or check == 'n'):  # This for NO
		break

	elif(check == 'Y' or check == 'y'):	#This for YES
		continue

print("\n")
honor_students = list ()   # To store the list of Honor students

for stu in student_info:
	print ("Student id: ", stu, "\t GPA: ", end = '')
	grades = 0
	credit = 0
	
	for j in student_info [stu]:
		grades += student_info [stu] [j] [0] * info_of_grade (student_info,j)
		credit += student_info [stu] [j] [0]

	print (round (grades / credit, 2))
 
	if grades / credit >= 3.0:		# Grades / credit is greater than or equal 3.0 then can be honor student
		honor_students.append (stu)

print ("\nHonor Students with GPA above 3.0:")
for stu in honor_students:
	print (stu)
