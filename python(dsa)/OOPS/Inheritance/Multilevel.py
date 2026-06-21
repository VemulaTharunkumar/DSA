class Student:
    def __init__(self,rno,name,branch,section):
        self._rno=rno
        self._name=name
        self._branch=branch
        self._section=section
class marks(Student):
    l=[]
    def __init__(self, rno, name, branch, section,m1,m2,m3):
        super().__init__(rno, name, branch, section)
        self._m1=m1
        marks.l.append(self._m1)
        self._m2=m2
        marks.l.append(self._m2)
        self._m3=m3
        marks.l.append(self._m3)
class Reports(marks):
    def __init__(self, rno, name, branch, section,m1,m2,m3):
        super().__init__(rno, name, branch, section,m1,m2,m3)
    def report(self):
        grades = []
        for x in marks.l:
            if x >= 90:
                grade = 10
            elif x >= 80:
                grade = 9
            elif x >= 70:
                grade = 8
            else:
                grade = 7
            grades.append(grade)
        self.total_marks = sum(marks.l)
        self.total_grade_points = sum(grades)
        self.cgpa = self.total_grade_points / len(grades) 
    def display(self):
        print("-------Student Details-------")
        print("Roll No:",self._rno)
        print("Name :",self._name)
        print("Branch :",self._branch)
        print("Section :",self._section)
        print("Total :",self.total_marks)
        print("Grade pointa :",self.total_grade_points)
        print("CGPA :",self.cgpa)
        
    
r=Reports(2,"Srujan","CSE","B",90,88,100)
r.report()
r.display()        