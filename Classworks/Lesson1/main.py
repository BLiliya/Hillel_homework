# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


my_age = 10
print(id(my_age))

my_age = 20
print(id(my_age))

age = 20  # int
name = 'Liliya'  # str
money = 20.12  # float
is_maried = False  # bool
car_model = None  # none

friends = [1, 2, 5, 3, 9, 1]  # list - changeable
old_friends = (1, 2, '12', False)  # tuple - not changeable
new_friends = {1, 'asd', False, 9, 1}  # set - unique values
vocab = {'name': 'Liliya', 'age': 20, 'voc2': {1: 2}}  # dictionary

print(vocab)

vocab.update({1: 2})
vocab['new_key'] = 'value'

friends.sort()
print(friends)
print(vocab)

age1 = '20'

john_salary = 50000.456
marta_salary = 50001.654

print(john_salary, marta_salary)

john_age = 25
marta_age = 23

print(john_age, marta_age)


john_name = 'John'
marta_name = 'Marta'

print(john_name, marta_name)

john_gender = False
marta_gender = True

print(john_gender, marta_gender)

john_friends = ['James', 'Peter', 'Scott', 'Lucy']
marta_friends = ['Julia', 'Maria', 'Jessy', 'Barbara']
print(john_friends, marta_friends)

names_list = ['Balin','Durin', 'Thorin', 'Dwalin', 'Gloin', 'Kili', 'Thorin', 'Balin']
print(names_list)

names_set = set(names_list)
print(names_set)

