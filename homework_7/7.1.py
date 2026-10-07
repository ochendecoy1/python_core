# Создайте класс CreditCard, описывающий кредитную карту. При
# создании объекта необходимо передавать номер счёта и начальный
# баланс карты. Реализуйте метод deposit(amount), который пополняет
# баланс на указанную сумму, метод withdraw(amount), который снимает
# указанную сумму, и метод show_info(), который выводит номер счёта и
# текущий баланс.
# Создайте три объекта класса CreditCard с разными номерами счетов и
# начальными балансами. Пополните баланс первой и второй карты, а с
# третьей карты снимите некоторую сумму. После выполнения операций
# выведите информацию о состоянии всех трёх карт.

class CreditCard:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Карта {self.account_number} пополнена "
                  f"на {amount}. Балансаланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть положительной и больше нуля.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Сумма {amount} снята с карты {self.account_number}."
                  f" Текущий баланс: {self.balance}")
        elif amount > self.balance:
            print(f"Недостаточно средств на карте {self.account_number}."
                  f" Текущий баланс: {self.balance}")

    def show_info(self):
        print(f"Номер счёта: {self.account_number},"
              f" "f"Текущий баланс: {self.balance}")


card1 = CreditCard("1234-5678-9012-3456", 1000)
card2 = CreditCard("9876-5432-1098-7654", 200000)
card3 = CreditCard("5678-9012-3456-7890", 98765432)

card1.deposit(777)
card2.deposit(999999)
card3.withdraw(10000432)

print("\nИнформация о картах:\n")
card1.show_info()
card2.show_info()
card3.show_info()