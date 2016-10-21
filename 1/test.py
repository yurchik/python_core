# foods = ['bacon', 'tuna', 'ham', 'snousages', 'beef']
#
# for f in foods[2:4]:
#     print(f)
#     print(len(f))
#
# for f in range(5, 17, 3):
#     print(f)

magicNumber = 26

# print('Yurchik', 54)

# ok, this program will find the magic number

for i in range(101):
    if i is magicNumber:
        print(i, 'is the magic number!')
        break
    else:
        if i % 4 == 0:
            print(i)
