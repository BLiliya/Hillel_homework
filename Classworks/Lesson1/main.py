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
