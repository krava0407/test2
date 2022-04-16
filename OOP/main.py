
from human import Human
from house import House
from smallHouse import Small_House

if __name__ == '__main__':
     Human.def_info()

     alex = Human(27, 'Alex')
     alex.info()

     sh = Small_House(15_000)
     alex.buy_house(sh, 10)

     alex.earn_money(5_000)
     alex.buy_house(sh, 10)
     alex.info()

     alex.earn_money(15_000)
     alex.buy_house(sh, 10)
     alex.info()