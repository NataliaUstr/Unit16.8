class Castomers:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'"{self.name} {self.surname}.{self.city}.Баланс: {self.balance} руб."'


    def get_list (self):
        return f'"{self.name} {self.surname}.{self.city}"'


cast_1 = Castomers("Иван", "Петров", "Москва", 50)
cast_2 = Castomers("Николай", "Чичиков", "Самара", 60)
cast_3 = Castomers("Игорь", "Суворов", "Пенза", 70)
cast_4 = Castomers("Сергей", "Уткин", "Псков", 80)

print("\n",cast_1,"\n",cast_2,"\n",cast_3,"\n",cast_4,"\n")

castomers_list=[cast_1,cast_2,cast_3,cast_4]


for castomers in castomers_list:
    print(castomers.get_list())