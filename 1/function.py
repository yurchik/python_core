# def beef():
#     print('Dayum? this function are relly cool!')
#
# def bitcoint_to_usd(btc):
#     amount = btc * 527
#     print(amount)
#
# bitcoint_to_usd(3)
#
# def allow_dating_age(age):
#     girl_age = age/2 + 7
#     return girl_age
#
# for lim in range(15, 60):
#     limit = allow_dating_age(lim)
#     print(lim, "yaer old can date with", limit, "or older")
#
# def get_gender(sex='unknown'):
#     if sex is 'm':
#         sex = 'Male'
#     elif sex is 'f':
#         sex = 'Female'
#     print(sex)
#
# get_gender('m')
# get_gender('f')
# get_gender()

# def some_nums(*args):
#     total = 0
#     for a in args:
#         total += a
#     return total
#
# print(some_nums(1, 3, 45, 656, 76, 45))

def health_calculator(age, apple_eat, sig_smoke):
    answer = (100 - age) + (apple_eat * 3.5) - (sig_smoke * 2)
    print(answer)

yurchik_data = [27, 10, 0]

health_calculator(*yurchik_data)