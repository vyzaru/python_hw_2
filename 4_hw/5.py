class Deck_Iterator:

    def __init__(self):
        self.increment = 0
        self.suits = ['Черви', 'Пик', 'Бубны', 'Крести']
        self.card = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        self.quantity_cards = len(self.suits) * len(self.card)

    def __iter__(self):
        return self

    def __next__(self):
        if self.increment >= 52:
            raise StopIteration
        suit = self.suits[self.increment // len(self.card)]
        card = self.card[self.increment % len(self.card)]
        self.increment += 1
        return f"{card} {suit}"


deck = Deck_Iterator()
for c in deck:
    print(c)
