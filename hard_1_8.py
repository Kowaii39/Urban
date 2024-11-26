grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(students)

i = 0

grades_of_student = {}

while i < len(grades):
    num = grades[i]
    name = students[i]
    i = i + 1
    n = sum(num)
    o = len(num)
    average = n / o
    if i > len(grades):
        break
    grades_of_student[name] = average

print(grades_of_student)

