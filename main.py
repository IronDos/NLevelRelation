from Person import Person
from Name import Name
from Address import Address

def FindAllDirectRelation(p1, persons):
  directRelationPersons = []
  for p in persons:
    if (Person.isDirectRelation(p1, p)):
      directRelationPersons.append(p)
  return directRelationPersons

def FindMinRelationLevel(p1, p2, persons):
  counter = 1

  if (Person.isDirectRelation(p1, p2)):
    return 1

  for i in range(0, len(persons)):
    allR = FindAllDirectRelation(p1, persons)

    if (allR != []):
      for j in range(0, len(allR)):
        if (Person.isDirectRelation(p2, allR[j])):
          return counter+1
      p1 = allR[0]
      persons.remove(allR[0])
      counter+=1
  return -1


def Init(persons = []):
  p1 = Person(Name('Alan', 'Turing'), Address('Bletchley Park', 'Bletchley Park'))
  p2 = Person(Name('Alan', 'Turing'), Address('Cambridge', 'Cambridge'))
  p3 = Person(Name('Joan', 'Clarke'), Address('Bletchley Park', 'Bletchley Park'))
  p4 = Person(Name('Joan', 'Clarke'), Address('London', 'London'))
  p5 = Person(Name('Grace', 'Hopper'), Address('New York', 'New York'))
  persons.extend((p1, p2, p3, p4, p5))
  
  print('MinRelationLevel:' + str(FindMinRelationLevel(p1, p4, persons)))


Init()