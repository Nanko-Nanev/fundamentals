n = int(input())
students = {}
students_with_average_grades = {}

for i in range(n):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.5:
        students_with_average_grades[name] = average_grade

for name, grades in sorted(students_with_average_grades.items(), key=lambda x: x[1], reverse=True):
    print(f"{name} -> {grades:.2f}")
