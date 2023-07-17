# Course Management System

# Course details
course = {}

# List of students
students = []

# Function to add a course
def add_course(name, duration, modules, fee):
    course['name'] = name
    course['duration'] = duration
    course['modules'] = modules
    course['fee'] = fee

# Function to add students
def add_student(name, fee):
    students.append({'name': name, 'fee': fee})

# Function to display the course details
def display_course():
    print("Course Name:", course['name'])
    print("Course Duration:", course['duration'])
    print("Course Modules:", course['modules'])
    print("Course Fee:", course['fee'])

# Function to display the students
def display_students():
    for student in students:
        print("Student Name:", student['name'])
        print("Student Fee:", student['fee'])

# Test the functions
add_course('Python Programming', '3 months', ['Introduction', 'Advanced Concepts', 'Project'], 500)
add_student('John Doe', 500)
display_course()
display_students()
