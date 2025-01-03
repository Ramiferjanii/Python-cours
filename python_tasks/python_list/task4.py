if __name__ == '__main__':
    student=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        student.append([name , score]) 
        unique_grades = sorted(set([score for name, score in student]))
    
    # Find the second lowest grade
    second_lowest_grade = unique_grades[1]
    
    # Find all students with the second lowest grade
    second_lowest_students = [name for name, score in student if score == second_lowest_grade]
    
    # Sort the students' names alphabetically
    second_lowest_students.sort()
    
    # Print each student's name on a new line
    for student in second_lowest_students:
        print(student)
    

"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line."""