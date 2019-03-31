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
        self.__wagon_cards = list()
        self.__rejected_wagon_cards = list()
        self.__add_wagons(WagonTypes.locomotive, 6)
        self.__add_wagons(WagonTypes.blue_wagon, 2)
        self.__add_wagons(WagonTypes.yellow_wagon, 2)
        self.__add_wagons(WagonTypes.white_wagon, 2)
        self.__add_wagons(WagonTypes.black_wagon, 2)
        self.__add_wagons(WagonTypes.orange_wagon, 2)
        self.__add_wagons(WagonTypes.green_wagon, 2)
        self.__add_wagons(WagonTypes.red_wagon, 2)
        self.__add_wagons(WagonTypes.pink_wagon, 2)
        self.__shuffle_wagons_cards()

    def __add_wagons(self, wagon_type, how_many):
        new_wagons = how_many * [wagon_type]
        self.__wagon_cards.extend(new_wagons)

    def __swap(self, wagon_cards, index_1, index_2):
        wagon_cards[index_1], wagon_cards[index_2] = wagon_cards[index_2], wagon_cards[index_1]

    def __shuffle_wagons_cards(self):
        for i in range(3847):
            random_1 = random.randint(0, len(self.__wagon_cards) - 1)
            random_2 = random.randint(0, len(self.__wagon_cards) - 1)
            self.__swap(self.__wagon_cards, random_1, random_2)        

    def pop(self):
        if not self.__wagon_cards:
            self.__wagon_cards, self.__rejected_wagon_cards = self.__rejected_wagon_cards, self.__wagon_cards
            self.__rejected_wagon_cards.clear()
            if len(self.__wagon_cards) > 1:
                self.__shuffle_wagons_cards()

        if not self.__wagon_cards:
            return None

        return self.__wagon_cards.pop()

    def reject(self, wagon_card):
        if wagon_card != None:
            self.__rejected_wagon_cards.append(wagon_card)

    def print_deck(self):
        print('main deck: ')

        for card in self.__wagon_cards:
            print(card)

        print('rejected: ')

        for card in self.__rejected_wagon_cards:
            print(card)
    
        
deck = WagonsDeck()

def flip_coin():
    return random.randint(0, 1) == 0

for i in range(0, 500):

    deck.print_deck()

    card1 = deck.pop()
    card2 = deck.pop()

    print('Got ' + str(card1) + ' and ' + str(card2))

    if flip_coin():
        print('Rejecting ' + str(card1))
        deck.reject(card1)
    else:
        print('Rejecting ' + str(card2))
        deck.reject(card2)

    print('-----------------------------------------------------------')
    nothing = input()



