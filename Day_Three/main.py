food = input('Name a food >')
plant = input('Name a plant >')
cooking_method = input('a method of cooking >')
burnt_desc = input('Describe the taste of burnt food in one word >')
house_hold_item = input('Name a house hold item >')

print("""
         MENU
{0} {1} underneath {2} {3} 
with a side of {4}
""".format(cooking_method,food,burnt_desc, plant,house_hold_item))