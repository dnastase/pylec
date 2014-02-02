#!/usr/bin/env python

class Person:
   def __init__(self, name, ident):
      self.name = name
      self.ident = ident

class Course:
   def __init__(self, title, info):
      self.title = title
      self.info = info

class Student(Person):
   def __init__(self, name, id, lCourses):
      Person.__init__(self, name, id)
      self.lCourses = lCourses
      self.dCourse2Info = {}
      self.dCourse2Grade = {}
      self.homework = None

   def learn(self, aCourse):
      self.dCourse2Info[aCourse] = aCourse.info

   def setGrade(self, aCourse, grade):
      self.dCourse2Grade[aCourse] = grade

class Teacher(Person):
   def __init__(self, name, id, aCourse):
      Person.__init__(self, name, id)
      self.course = aCourse

   def teach(self, lStudents):
      for student in lStudents:
         student.learn(self.course)

   def grade(self, lStudents):
      for student in lStudents:
         grade = listen(student)
         student.setGrade(self.aCourse, grade)

   def listen(self, aStudent):
      grade = calcGrade(aStudent.homework)
      return grade

math = Course("Math", "knowledge about math ...")
stats = Course("Statistics", "stats know-how")

john = Student("John", 12, [math, stats])
mary = Student("Mary", 34, [stats,])
allStudents = [john, mary]

stats_prof  = Teacher("Brad", 56, stats)
math_prof = Teacher("Ellen", 78, math)
allTeachers = [stats_prof, math_prof]

allPeople = allStudents + allTeachers

for p in allPeople:
   print(p.name, p.ident)

stats_prof.teach(allStudents)

