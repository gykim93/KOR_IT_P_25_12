# class Warrior():
#   def __init__(self, hp, mp, attack_point):
#       self.hp = hp
#       self.mp = mp
#       self.attack_point = attack_point

#   def attack(self):
#       print("공격!")

# x = Warrior(1000,500,30)

# print(x.hp,x.mp,x.attack_point)

# x.attack()
# # 출력 : 공격!


class Warrior:
    def attack(self):
        print("공격!")


x = Warrior()
x.hp = 1000
x.mp = 500
x.attack_point = 30

print(x.hp, x.mp, x.attack_point)

x.attack()
# 출력 : 공격!
