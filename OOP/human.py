

class Human:
    def_name = 'Anonim'
    def_age = 35

    def __init__(self, age=def_age, name=def_name):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'name = {self.name}, age = {self.age},money = {self.__money}, house = {self.__house}')

    @staticmethod
    def def_info():
        print(f'def_age = {Human.def_age} def_name = {Human.def_name}')

    def __make_deal(self, price, house):
        self.__money -= price
        self.__house = house
        return self.__money

    def earn_money(self, amount):
        self.__money += amount
        return print(f'Earned {amount}. Current value: {self.__money}')

    def buy_house(self, house, discount: int):
        price = house.final_price(discount=discount)

        if self.__money >= price:
            self.__make_deal(price, house)
            print('Accepted!')
        else:
            print('No enough money!')
