from house import House

class Small_House(House):

    def_area = 40

    def __init__(self, price):
        super().__init__(Small_House.def_area, price)
