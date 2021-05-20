class Address:
  def __init__(self, street, city):
    self.street = street
    self.city = city
  def __str__(self):
    return 'Address:\n' + ' - Street:' + self.street +  '\n - City:' + self.city