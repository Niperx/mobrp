

class Soldier:


    def __init__(self, name, level, role, inventory):
        self.name = name
        self.level = level
        self.role = role
        self.inventory = inventory

    def info(self):
        print(f'Имя: {self.name}')
        print(f'Уровень: {self.level}')
        print(f'Специализация: {self.role}')
        print(f'Инвентарь: {self.inventory}')



def main():
    x = input()
    if '/new' in x:
        name = x[x.find(' ')+1:]
        hero = Soldier(name, 1, None, None)
        hero.info()




if __name__ == "__main__":
    main()