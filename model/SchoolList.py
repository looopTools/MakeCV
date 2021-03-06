from school import school


class SchoolList:

    def __init__(self):
        self.schools = list()

    def addSchool(self, s):
        if isinstance(s, school):
            self.schools.append(s)
            print('School has been added')
        else:
            print('Only added a objects of type school')

    def getKey(self, item):
        return item.endDate

    def getSchoolsByEndDate(self):
        return sorted(self.schools, key=self.getKey)

    def printList(self):
        for s in self.schools:
            s.printAll()
