students = {}

def add_student(name):
    students[name] = []

def record_grade(name, grade):
    if name in students: 
        students[name].append(grade) 
    else: 
        print(f"Student '{name}' not found.")

def calculate_average_grade(name):
    if name in students: 
        grades = students[name] 
        if len(grades) == 0: 
            return 0 
        return sum(grades) / len(grades) 
    else: 
        print(f"Student '{name}' not found.")
        return 0

def display_student_info(name): 
    if name in students: 
        avg_grade = calculate_average_grade(name) 
        print(f"Student Name: {name}") 
        print(f"Grades: {students[name]}") 
        print(f"Average Grade: {avg_grade:.2f}")
    else: 
        print(f"Student '{name}' not found.")

add_student("Maya")
record_grade("Maya", 85) 
record_grade("Maya", 92) 
display_student_info("Maya")