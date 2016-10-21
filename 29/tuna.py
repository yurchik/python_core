class Enemy:

    gender = 'male'

    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(200)
jastin = Enemy(20)

jason.get_energy()
print(jason.gender)

jastin.get_energy()
print(jastin.gender)