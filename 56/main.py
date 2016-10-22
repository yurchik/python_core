from operator import attrgetter


class User:

    def __init__(self, x, y):
        self.name = x
        self.id = y

    def __repr__(self):
        return self.name + "\t: " + str(self.id)


users = [
    User('Sasha', 11),
    User('Dasha', 12),
    User('Pasha', 13),
    User('Kasha', 14),
    User('Masha', 15),
    User('Glasha', 16)
]

for user in users:
    print(user)

print('---------------')

for user in sorted(users, key=attrgetter('id')):
    print(user)