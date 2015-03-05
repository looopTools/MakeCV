from entity import entity
from school import school
from work import work

from SchoolList import SchoolList

class cv:

    def __init__(self, firstName, lastName):

        self.firstName = firstName
        self.lastName = lastName

        self.shortDescription = ''

        self.schoolList = SchoolList()
        self.workLiist = []


    def getFullName(self):
        return self.firstName + self.lastName
