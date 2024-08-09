# hero.py

class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print_name(self):
        print(f"Имя героя: {self.name}")

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


# Создание объекта класса SuperHero и применение методов
hero = SuperHero(
    name="Бэтмен",
    nickname="Темный рыцарь",
    superpower="Высокий интеллект",
    health_points=100,
    catchphrase="Я Бэтмен!"
)

hero.print_name()
hero.double_health()
print(hero)  # Вывод прозвища, суперспособности и здоровья
print(f"Длина коронной фразы: {len(hero)}")

