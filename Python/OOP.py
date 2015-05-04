class Subjects(object):
    def __init__(self, subject_name, teacher):
        self.subject =+ subject_name
        self.teacher_inCharge = teacher

    def get_subject(self):
        return self.subject
    def teacher(self):
        return self.teacher_inCharge

class Student(Subjects):
    def __init__(self, name, *args):
        self.name = name
        self.lst = list(args)

    def getStudent(self):
        return self.name

    def Subjects(self):
        self.Subjects += self.lst

class Teachers(Student, Subjects):
    def __init__(self, teacher_name):
        self.teacher = teacher_name

    def get_teacher(self):
        return self.teacher


