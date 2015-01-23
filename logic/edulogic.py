from model.Entity import *
from model.School import *
class edulogic:

    def __init__(self):
        self.educations = []

    def CreateSchool(self, info_dic):
        s = School()
        s.assing_var(info_dic)
        s.printSchool()
        self.educations.append(s)
