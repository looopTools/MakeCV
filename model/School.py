class School:

    def __init__(self):
        self.school = ''
        self.startYear = -1
        self.endYear = -1
        self.title = ''
        self.description = ''
        self.complet = False

    def assing_var(self, dic):
        self.school = dic['school']
