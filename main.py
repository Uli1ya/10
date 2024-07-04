from _class import Class
from student import Student
from teacher import Teacher
#commit

T1 = Teacher("Т", "И", ['Физкультура'])
print(T1._subjects)
S1 = Student("В", "П")
S2 = Student("А", "Б")
S3 = Student("У", "М")
C1 = Class(Teacher1, [Student1, Student2, Student3])
print(len(C1))

T1.set_class(C1)
print(T1.get_class())
S3.set_class(C1)

T2 = Teacher("Р", "М", ['Биология', 'Физика'])
S4 = Student("Е", "Ф")