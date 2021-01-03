command = input().split(" : ")
courses = {}

while not command[0] == "end":
    course_name = command[0]
    student_name = command[1]
    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)
    command = input().split(" : ")

courses = dict(sorted(courses.items(), key=lambda x: -len(x[1])))
for course_names, student_names in courses.items():
    print(f"{course_names}: {len(courses[course_names])}")
    # student_names = [student_names for i in sorted(courses.values())]
    student_names_sorted = sorted(student_names)
    for i in range(len(courses[course_names])):
        print(f"-- {student_names_sorted[i]}")


# for names in courses:
#     print(f"{names}: {len(courses[names])}")
#     for students in courses.items():
#         print(f"-- {courses[students[0]]}")
#         courses.pop(students[0])

