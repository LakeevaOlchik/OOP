class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_r(self):
        list_grade = []
        for v in self.grades.values():
            for list_gr in v:
                list_grade.append(list_gr)
        sum_lst = sum(list_grade)
        avr_rating = round(sum_lst / len(list_grade), 2)
        return avr_rating

    def rate_lesson(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
     if not isinstance(other, Student):
         print('Not initialize other student')
         return
     if not isinstance(self, Student):
         print('Not initialize self student')
         return
     if self.average_r() > other.average_r():
         print(f'{self.name} имеет больший бал чем {other.name}')
     else:
         print(f'{other.name} имеет больший бал чем {self.name}')


    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за домашние задания: {self.average_r()}\n" \
              f"Курсы в процессе обучения: {self.courses_in_progress}\n" \
              f"Завершенные курсы: {self.finished_courses}"
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = 0
        self.students_list = []

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        elif self.average_rating < other.average_rating:
            print(f"{self.name} имеет больший бал, чем {other.name}")
        else:
            print(f"{other.name} имеет больший бал, чем {self.name}")

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за лекции: {self.average_rating}"
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

        sum = 0
        len = 0

        for key in student.grades.keys():
            for grad in list(student.grades[key]):
                sum += grad
                len += 1
            student.average_rating = round(sum / len, 2)

    def __str__(self):
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}"
        return res


student1 = Student('Артем', 'Петров', 'м')
student1.finished_courses += ['Python для начинающих']
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['git']

student2 = Student('Ольга', 'Иванова', 'ж')
student2.finished_courses += ['Python для начинающих']
student2.courses_in_progress += ['git']

lecturer1 = Lecturer('Генрих', 'Четвертый')
lecturer1.courses_attached += ['git']
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Альберт', 'Локомотивов')
lecturer2.courses_attached += ['git']

reviewer1 = Reviewer('Семен', 'Слепаков')
reviewer1.courses_attached += ['git']

reviewer2 = Reviewer('Змей', 'Горыныч')
reviewer2.courses_attached += ['git']
reviewer2.courses_attached += ['Python']

# Задание 4/ полевые испытания

student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]


def average_rating_hw(students, courses):
    sum_course_grade = 0
    iterator = 0
    for student in students:
        for key, value in student.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)


def average_rating_lesson(lecturers, courses):
    sum_course_grade = 0
    iterator = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if courses in key:
                sum_course_grade += sum(value) / len(value)
                iterator += 1
    return round(sum_course_grade / iterator, 2)


student1.rate_lesson(lecturer1, 'git', 8)
student1.rate_lesson(lecturer1, 'Python', 10)
student2.rate_lesson(lecturer1, 'git', 5)
student2.rate_lesson(lecturer1, 'Python', 5)
student1.rate_lesson(lecturer2, 'git', 6)
student2.rate_lesson(lecturer2, 'git', 8)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'git', 9)
reviewer1.rate_hw(student2, 'git', 7)
reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student1, 'git', 5)
reviewer2.rate_hw(student2, 'git', 10)

print('Список студентов:')
print(f"{student1}\n")
print(f"{student2}\n")
print('_______________')
print('Список лекторов:')
print(f"{lecturer1}\n")
print(f"{lecturer2}\n")
print('________________')
print("Cписок проверяющих:")
print(f"{reviewer1}\n")
print(f"{reviewer2}\n")

# подсчет средней оценки

print("______________")
print(f"средняя оценка студентов за курс Git: {average_rating_hw(student_list, 'git')}")
print(f"средняя оценка студентов за курс Python для продвинутых: {average_rating_hw(student_list, 'Python')}")
print(f"средняя оценка лекторов за курс Git: {average_rating_lesson(lecturer_list, 'git')}")
print(f"средняя оценка лекторов за курс Python для продвинутых: {average_rating_lesson(lecturer_list, 'Python')}")

# сравнение по средней оценке
print('_______________')
print('Сравнение среднего бала студентов:')
student1 < student2
print()
print('Сравнение среднего бала лекторов:')
lecturer1 < lecturer2


