list_money = [20, 50, 40]

def double_money(num):
    return num * 2

new_list = list(map(double_money, list_money))

print(new_list)