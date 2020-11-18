groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "Математика", "Программирование"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Константин",
        "surname": "Краснов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Алексей",
        "surname": "Степанов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Андрей",
        "surname": "Соловьев",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Руслан",
        "surname": "Расулов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 3, 3]
    },
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30),
              str(student["marks"]).ljust(20))


print_students(groupmates)


def count_mark(student, mark):
    print(u"name".ljust(15), u"surname".ljust(10), u"exams".ljust(30), u"marks".ljust(20))
    for student in student:
        marks_list = student['marks']
        result = (sum(marks_list) / len(marks_list))
        if result > mark:
            print(student["name"].ljust(15),
            student["surname"].ljust(10), str(student["exams"]).ljust(30),
            str(student["marks"]).ljust(20))


need = float(input('Input :'))

count_mark(groupmates, need)
