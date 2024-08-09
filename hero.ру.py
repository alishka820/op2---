# hero.py

class SuperHero:
    # Свойство класса
    people = 'people'

    # Конструктор класса
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    # Метод для вывода имени героя
    def print_name(self):
        print(f"Имя героя: {self.name}")

    # Метод для умножения здоровья героя на 2
    def double_health(self):
        self.health_points *= 2

    # Магический метод для вывода информации о герое
    def __str__(self):
        return f"Прозвище: {self.nickname}, Суперспособность: {self.superpower}, Здоровье: {self.health_points}"

    # Магический метод для подсчета длины коронной фразы героя
    def __len__(self):
        return len(self.catchphrase)


# Создание объекта класса SuperHero
if __name__ == "__main__":
    hero = SuperHero("Супермен", "Человек из стали", "Летать и сила", 100, "Правда, справедливость, американский путь")

    # Применение методов
    hero.print_name()
    hero.double_health()
    print(hero)
    print(f"Длина коронной фразы героя: {len(hero.catchphrase)}")
