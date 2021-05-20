class Person:
  def __init__(self, fullName, address):
    self.fullName = fullName
    self.address = address
  
  @staticmethod
  def isDirectRelation(p1, p2):
    if (p1.fullName.firstName == p2.fullName.firstName and p1.fullName.lastName == p2.fullName.lastName):
      return True
    if (p1.address.street == p2.address.street and p1.address.city == p2.address.city):
      return True
    return False
  
  def isEql(p1, p2):
    if (p1.fullName.firstName == p2.fullName.firstName and
    p1.fullName.lastName == p2.fullName.lastName and
    p1.address.street == p2.address.street and
    p1.address.city == p2.address.city):
      return True
    return False


  def __str__(self):
    return str('-----\n' + 'Person:\n' + str(self.fullName) + '\n' + str(self.address) + '\n-----')
  