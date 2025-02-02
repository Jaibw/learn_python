class Student:
    student_name = ""
    def __init__(self,name):
        self.student_name = name

    def getStudent(self):
        print(self.student_name)

    def updateStudentName(self,name):
        self.student_name = name
