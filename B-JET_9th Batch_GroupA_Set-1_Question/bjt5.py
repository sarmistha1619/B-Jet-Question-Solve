from abc import ABC,abstractmethod
class Students:
    def general_courses(self,Bangla,English):
        self.Bangla = Bangla
        self.English = English

    @abstractmethod
    def Special_courses(self):
        pass

    @abstractmethod
    def Optional_courses(self):
        pass

class CourseForA(Students):
    def Special_courses(self):
        pass
    def Optional_courses(self):
        pass

class CourseForB(Students):
    def Special_courses(self):
        pass
    def Optional_courses(self):
        pass
class CourseForC(Students, CourseForA):
    def Special_courses(self):
        pass
    def Optional_courses(self):
        pass

Group_A = CourseForA()
Group_A.general_courses()
Group_A.Special_courses()
Group_B  = CourseForB()
Group_B.Optional_courses()
Group_B.Special_courses()
Group_C  = CourseForC()
Group_C  = CourseForB()
Group_C.Optional_courses()

