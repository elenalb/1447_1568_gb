# пример решения ООП-задачи

# 1. Сформулировать задачу
# 2. Определить объекты для решения задачи
# 3. Выделить классы для формирования объектов
# 4. Определить атрибуты и методы классов
# 5. Создать классы, атрибуты, методы
# 6. Создать объекты классов
# 7. Выполнить итоговое решение

# Разработка виртуальной модели образовательного процесса.
# объекты: преподаватели, студенты, знания
# классы: class Person -> class Teacher, class Student. class Subject
# class Person: self.name, self.surname
# class Teacher: to_teach()
# class Student: to_take(), self.knowledge = []
# class Subject: self.subjects = [], subject_list()


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"


class Teacher(Person):
    def to_teach(self, subject, *students):
        for student in students:
            student.to_take(subject)


class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledge = []

    def to_take(self, subject):
        self.knowledge.append(subject)


class Subject:
    def __init__(self, *subjects):
        self.subjects = list(subjects)

    def subject_list(self):
        return self.subjects


s = Subject("python", "maths")
t = Teacher("Elena", "Babenko")
print(t)

student1 = Student("Ivan", "Ivanov")
student2 = Student("Petr", "Petrov")
student3 = Student("Misha", "Mishin")

print(f"{student1}, {student2}, {student3}")
t.to_teach(s, student1, student2, student3)

for subject in student1.knowledge:
    print(subject.subject_list())

for subject in student2.knowledge:
    print(subject.subject_list())


import gc
for i in gc.get_referrers(Student):
    if i.__class__ is Student:
        print(i)
