import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print("{} of {}".format(self.val,self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(v,s))

    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle(self):
        for i in range(1,len(self.cards)):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCards(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCards())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

if __name__ == "__main__":
    deck =Deck()
    deck.shuffle()
    jas = Player("Jas")
    jas.draw(deck)
    jas.draw(deck)
    jas.draw(deck)
    jas.showHand()