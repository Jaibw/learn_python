from students import Student
from mylogic import total
from mylogic import Mylogic

s1 = Student("jai")
s1.getStudent()
s1.updateStudentName("vijay")
s1.getStudent()

print(total(1,2))

ml1 = Mylogic()
print(ml1.total(1,2))
print(ml1.total(3,1))
print(ml1.getUsed())
