class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name +' menu available from '+str(self.start_time)+' to '+str(self.end_time)

  def calculate_bill(self,purchased_items):
    bill = 0
    for p in purchased_items:
      bill += self.items[p]
    return bill

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return self.address
  
  def available_menus(self, time):
    av = []
    for m in self.menus:
      if m.start_time <= time and m.end_time >= time:
        av.append(m.name)
    return av

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

m1 = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu('brunch', m1, 11, 16)
m2 = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu('early bird', m2, 15, 18)
m3 = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu('dinner', m3, 17, 23)
k = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu('kids',k,11,21)

a = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu('arepas_menu', a, 10, 20)

print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

flagship_store = Franchise('1232 West End Road',[brunch, early_bird, dinner, kids])

new_installment = Franchise('12 East Mulberry Street',[brunch, early_bird, dinner, kids])

print(flagship_store.available_menus(17))

arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)

business_1 = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

business_arepa = Business("Take a' Arepa", arepas_place)