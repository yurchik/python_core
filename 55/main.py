from operator import itemgetter

users = [
    {'fname': 'Yurchik', 'lname': 'Alex'},
    {'fname': 'Yana', 'lname': 'Alex'},
    {'fname': 'Gosha', 'lname': 'Guk'},
    {'fname': 'Yurchik', 'lname': 'Hastler'},
    {'fname': 'Jeka', 'lname': 'Jones'},
    {'fname': 'Sveta', 'lname': 'Alex'},
    {'fname': 'Tomas', 'lname': 'Williams'},
    {'fname': 'Lila', 'lname': 'Hayat'},
    {'fname': 'Kasper', 'lname': 'Barbie'},
    {'fname': 'Yurchik', 'lname': 'Jones'}
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)