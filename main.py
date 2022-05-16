class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average(self):
        rate = []
        for courses, rates in self.grades.items():
            rate.extend(rates)
        if len(rate) != 0:
            average_rate = round(sum(rate)/len(rate), 2)
            return average_rate
        return 0

    def __str__(self):
        res = f""" 
        Имя: {self.name} 
        Фамилия: {self.surname} 
        Средняя оценка за домашние задания: {self.average()} 
        Курсы в процессе изучения: {",".join(self.courses_in_progress)} 
        Завершенные курсы: {",".join(self.finished_courses)} \n"""
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

    def average(self):
        return Student.average(self)

    def __lt__(self, other):
        if not isinstance(other, Student):
            return print('Нет такого студента')
        if self.average() < other.average():
            print(f'Средний балл выше у студента {other.name}')
        else:
            print(f'Средний балл выше у лектора {self.name}')
        return self.average() < other.average()

    def __str__(self):
        res = f""" 
        Имя: {self.name} 
        Фамилия: {self.surname} 
        Средняя оценка за лекции: {self.average()} \n"""
        return res

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f""" 
        Имя: {self.name} 
        Фамилия: {self.surname} \n"""
        return res

# Студенты и их курсы:
best_student = Student('Rudy', 'Sherman', 'male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.courses_in_progress += ['English']
best_student.finished_courses += ['Marketing']

student_one = Student('Shon', 'Perry', 'male')
student_one.courses_in_progress += ['Python']
student_one.courses_in_progress += ['Git']
student_one.finished_courses += ['Marketing']
student_one.finished_courses += ['English']

# Лекторы:
cool_mentor = Lecturer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Git']

lecturer = Lecturer('Slim', 'Shady')
lecturer.courses_attached += ['English']
lecturer.courses_attached += ['Git']

# Проверяющие:
reviewer = Reviewer('Ricky', 'Martin')
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Git']
reviewer.courses_attached += ['English']

reviewer_two = Reviewer('Big', 'Boss')
reviewer_two.courses_attached += ['Python']

# Студенты ставят оценки:
best_student.rate_hw(cool_mentor, 'Python', 10)
best_student.rate_hw(cool_mentor, 'Git', 7)
best_student.rate_hw(lecturer, 'English', 10)
best_student.rate_hw(lecturer, 'Git', 7)
student_one.rate_hw(cool_mentor, 'Python', 8)
student_one.rate_hw(cool_mentor, 'Git', 9)
student_one.rate_hw(lecturer, 'Python', 8) # лектор не ведет этот курс
student_one.rate_hw(lecturer, 'Git', 9)

# Проверяющие ставят оценки:
reviewer.rate_hw(student_one, 'Python', 7)
reviewer.rate_hw(student_one, 'Git', 6)
reviewer.rate_hw(student_one, 'English', 9) # у студента нет такого текущего курса
reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Git', 9)
reviewer.rate_hw(best_student, 'English', 9)
reviewer_two.rate_hw(student_one, 'Python', 4)
reviewer_two.rate_hw(best_student, 'Python', 9)
reviewer_two.rate_hw(best_student, 'English', 9) # не проверяет этот курс

# Принт персонажей:
print(student_one)
print(best_student)
print(cool_mentor)
print(lecturer)
print(reviewer)

print('-'*50)

# Сравнение средних оценок:
print(cool_mentor < best_student)
print(cool_mentor < student_one)

print('-'*50)

# Средний балл студентов по конкретному курсу:
students = [student_one, best_student]
def average_hw(all_students, course):
  rate = []
  for student in all_students:
      if course in student.grades.keys():
        rate.extend(student.grades.get(course))
        average_rate = round(sum(rate)/len(rate), 2)
  return print(f'Средний балл студентов по курсу {course}:', average_rate, 'баллов')
average_hw(students, 'Git')

print('-'*50)

# Средний балл лекторов по конкретному курсу:
lectures = [lecturer, cool_mentor]
def average_lect(all_lectures, course):
  rate = []
  for lector in all_lectures:
      if course in lector.grades.keys():
        rate.extend(lector.grades.get(course))
        average_rate = round(sum(rate)/len(rate), 2)
  return print(f'Средний балл лекторов по курсу {course}:', average_rate, 'баллов')
average_lect(lectures, 'Git')