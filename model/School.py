from Entity import *
#
class School(Entity):

    def __init__(self):
        Entity.__init__(self)
        self.startYear = -1
        self.endYear = -1
        self.complete = False

    def assing_var(self, dic):
        Entity.institution_name = dic['school']
        self.startYear = dic['startYear']
        self.endYear = dic['endYear']
        Entity.title = dic['title']
        Entity.description = dic['description']
        self.complete = dic['complete']

    def printSchool(self):
        print(Entity.institution_name)
        print(self.startYear)
        print(self.endYear)
        print(Entity.title)
        print(Entity.description)
        print(self.complete)
