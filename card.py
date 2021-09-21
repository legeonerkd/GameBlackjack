class Card:
    # Hearts - черви
    # Diamonds - бубны
    # Clubs - трефы (крести)
    # Spades - пики
    ICONS = {
        'H': '♥',
        'D': '♦',
        'S': '♠',
        'C': '♣',
    }
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    #! Возвращает данную строку вместо объекта, если попытаться его вывести
    def __str__(self):
        return self.value + Card.ICONS[self.suit]
    
    def __repr__(self):
        return self.__str__()