my_dict = {'Hanck':1990,'Bob':2000}
print(my_dict)
print(my_dict['Bob'],my_dict.get('Charly'))
my_dict['Max'] = 2001
my_dict['Anton'] = 1995
a = (my_dict.pop('Max'))
print(a)
print(my_dict)
my_set = {1,3,'coop',3,5,'coop',True}
print(my_set)
my_set.update({30,20,20})
my_set.remove(1)
print(my_set)