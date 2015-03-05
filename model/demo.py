from entity import entity
from school import school

from SchoolList import SchoolList

from cv import cv

from work import work
e = entity('p')
e.setStartDate('Jan 1 2005')
s = school('q')
s.setStartDate('Jan 1 2005')
s.setEndDate('Jan 1 2006')

s1 = school('q2')
s1.setStartDate('Jan 1 2005')
s1.setEndDate('May 29  2006')

w = work('w')
w.setStartDate('May 1 2014')

e.printName()
s.printAll()
w.printAll()


sl = SchoolList()

#sl.addSchool(e)
#sl.addSchool(w)
sl.addSchool(s1)
sl.addSchool(s)


print('List 1')
for x in range(0, len(sl.schools)):
    print(sl.schools[x].printAll())

l = sl.getSchoolsByEndDate()

print('List 2')
for x in range(0, len(l)):
    print(l[x].printAll())



cv1 = cv('Lol', 'Noob')
cv1.shortDescription = 'I am YMCA'
cv1.schoolList.addSchool(s)
cv1.schoolList.addSchool(s1)
print(cv1.firstName)
print(cv1.lastName)
print(cv1.shortDescription)
cv1.schoolList.printList()
