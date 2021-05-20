class Name:
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName
  def __str__(self):
    return 'FullName:\n' + ' - First Name:' + self.firstName +  '\n - Last Name:' + self.lastName