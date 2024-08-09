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

class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = False

    def print_name(self):
        print(f"Имя героя: {self.name}")

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True

    def true_in_phrase(self, true_phrase):
        print(f"True in the {true_phrase}")

    def __str__(self):
        return (f"Прозвище: {self.nickname}, Суперспособность: {self.superpower}, "
                f"Здоровье: {self.health_points}, Летает: {self.fly}")


# Воздушный герой
class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, air_speed):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.air_speed = air_speed

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True


# Земной герой
class EarthHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, earth_strength):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.earth_strength = earth_strength

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True


# Космический герой
class SpaceHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, space_vision):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.space_vision = space_vision

    def double_health(self):
        self.health_points = self.health_points ** 2
        self.fly = True


# Создаем объекты для новых классов
air_hero = AirHero('Ветер', 'Соколиный Глаз', 'Суперскорость', 1500, 'Ветер всегда со мной!', 300, 'Высокая')
earth_hero = EarthHero('Гор', 'Титан', 'Суперсила', 2000, 'Я несокрушим!', 500, 'Мощь Земли')
space_hero = SpaceHero('Звездочет', 'Космический Страж', 'Космическое зрение', 1800, 'Звезды укажут путь!', 400, 'Острый взгляд')

# Вызов новых методов
air_hero.double_health()
earth_hero.double_health()
space_hero.double_health()

air_hero.true_in_phrase('Wind powers everything!')
earth_hero.true_in_phrase('Strength of the Earth is unstoppable!')
space_hero.true_in_phrase('The stars are my guide!')

print(air_hero)
print(earth_hero)
print(space_hero)


# Создаем класс Villain
class Villain(SuperHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, target):
        if hasattr(target, 'damage'):
            target.damage **= 2


# Создаем объект злодея и применяем метод crit на героя
villain = Villain('Морок', 'Темный Лорд', 'Темные силы', 3000, 'Тьма поглотит всех!', 600)
villain.crit(air_hero)

print(f"Урон воздушного героя после атаки злодея: {air_hero.damage}")
