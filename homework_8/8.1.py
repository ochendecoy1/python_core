# Разработать программу для работы с цветами и букетами, используя
# принципы объектно-ориентированного программирования.
# Необходимо:
# ● Определить иерархию классов цветов и реализовать несколько
# различных видов цветов.
# ● Для каждого цветка предусмотреть основные характеристики: название,
# стоимость и время жизни.
# ● Реализовать возможность собирать букет из разных цветов.
# ● Добавить в букет возможность использования аксессуаров и учитывать
# их стоимость при расчете общей стоимости букета.
# ● Реализовать метод для определения общей стоимости букета.
# ● Определить время увядания букета на основании среднего времени
# жизни всех цветов, входящих в него.
# ● Реализовать возможность сортировки цветов в букете по стоимости.
# ● Реализовать возможность проверить, присутствует ли определённый
# цветок в букете.
# При выполнении задания использовать классы, наследование, композицию и
# методы объектов

class Flower:
    def __init__(self, name: str, price: float, life_days: int):
        self.name = name
        self.price = price
        self.life_days = life_days

    def info(self) -> str:
        return f"{self.name} ({self.price} руб., {self.life_days} дн.)"


class Rose(Flower):
    def __init__(self):
        super().__init__(name="Ландыш", price=150.0, life_days=7)


class Tulip(Flower):
    def __init__(self):
        super().__init__(name="Тюльпан", price=90.0, life_days=5)


class Lily(Flower):
    def __init__(self):
        super().__init__(name="Пион", price=220.0, life_days=10)


class Accessory:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def info(self) -> str:
        return f"{self.name} (+{self.price} руб.)"


class Bouquet:
    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower: Flower):
        self.flowers.append(flower)

    def add_accessory(self, accessory: Accessory):
        self.accessories.append(accessory)

    def total_price(self) -> float:
        flowers_sum = sum(f.price for f in self.flowers)
        accessories_sum = sum(a.price for a in self.accessories)
        return flowers_sum + accessories_sum

    def average_life_days(self) -> float:
        if not self.flowers:
            return 0.0
        total_life = sum(f.life_days for f in self.flowers)
        return total_life / len(self.flowers)

    # сортировка цены по возрастанию
    def sort_by_price(self):
        self.flowers.sort(key=lambda f: f.price)

    # проверка наличия конкретного цветка
    def has_flower(self, flower_name: str) -> bool:
        for f in self.flowers:
            if f.name == flower_name:
                return True
        return False

    def summary(self) -> str:

        if not self.flowers:
            flowers_part = "нет цветов"
        else:
            flowers_part = ", ".join(f.info() for f in self.flowers)

        if not self.accessories:
            accessories_part = "нет аксессуаров"
        else:
            accessories_part = ", ".join(a.info() for a in self.accessories)

        return f"Букет: [{flowers_part}] + [{accessories_part}]"


rose1 = Rose()
rose2 = Rose()
tulip = Tulip()
lily = Lily()

ribbon = Accessory("Лента", 50.0)
box = Accessory("Коробка", 200.0)

bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(tulip)
bouquet.add_flower(lily)
bouquet.add_accessory(ribbon)
bouquet.add_accessory(box)

print(bouquet.summary())
print("Общая стоимость:", bouquet.total_price(), "руб.")
print("Среднее время жизни букета:", bouquet.average_life_days(), "дней")

bouquet.sort_by_price()
print("После сортировки по стоимости:", bouquet.summary())

print("Есть ли в букете Роза?", bouquet.has_flower("Роза"))
print("Есть ли в букете Пион?", bouquet.has_flower("Пион"))
