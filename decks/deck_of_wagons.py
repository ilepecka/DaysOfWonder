from enum import Enum
import random

class WagonTypes(Enum):
    locomotive = 0
    blue_wagon = 1
    yellow_wagon = 2
    white_wagon = 3
    black_wagon = 4
    orange_wagon = 5
    green_wagon = 6
    red_wagon = 7
    pink_wagon = 8

class WagonsDeck:

    def __init__(self):
        self.wagon_cards = list()
        self.__add_wagons__(self.wagon_cards, WagonTypes.locomotive, 16)
        self.__add_wagons__(self.wagon_cards, WagonTypes.blue_wagon, 12)
        self.__add_wagons__(self.wagon_cards, WagonTypes.yellow_wagon, 12)
        self.__add_wagons__(self.wagon_cards, WagonTypes.white_wagon, 12)
        self.__add_wagons__(self.wagon_cards, WagonTypes.black_wagon, 12)
        self.__add_wagons__(self.wagon_cards, WagonTypes.orange_wagon, 12)
        self.__add_wagons__(self.wagon_cards, WagonTypes.green_wagon, 12)
        self.__add_wagons__(self.wagon_cards, WagonTypes.red_wagon, 12)
        self.__add_wagons__(self.wagon_cards, WagonTypes.pink_wagon, 12)
        self.__shuffle__(self.wagon_cards)

    def __add_wagons__(self, karty_wagonow, wagon_type, how_many):
        new_wagons = how_many * [wagon_type]
        karty_wagonow.extend(new_wagons)

    def __swap__(self, karty_wagonow, index_1, index_2):
        karty_wagonow[index_1], karty_wagonow[index_2] = karty_wagonow[index_2], karty_wagonow[index_1]

    def __shuffle__(self, karty_wagonow):
        for i in range(3847):
            random_1 = random.randint(0, len(karty_wagonow) - 1)
            random_2 = random.randint(0, len(karty_wagonow) - 1)
            self.__swap__(karty_wagonow, random_1, random_2)        

    def pop(self, how_many):
        return WagonTypes.locomotive

    def put_back(self, wagon):
        pass

    def print_deck(self):
        for card in self.wagon_cards:
            print(card)
    
        
deck = WagonsDeck()
deck.print_deck()

