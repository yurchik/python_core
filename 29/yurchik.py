class Enemy:
    life = 3

    def attack(self):
        print('ouch!')
        self.life -= 1

    def checkLife(self):
        if (self.life <= 0):
            print('I am dead')
        else:
            print(self.life, 'life left')


attack = Enemy()
attack.attack()
attack.attack()
attack.attack()
attack.checkLife()