'''class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
The __init__ method is always just so formulaic. It takes the self parameter and all the attributes and you have to load them up yourself. There must be a better way. That is the dataclasses'''

from dataclasses import dataclass

@dataclass (frozen= True)
class Card:
    suit: str
    rank: int

    def __post_init__(self):  #this needs to be within the class, se mueve un espacio 
        if self.suit not in ("S", "H", "D", "C"):
            raise ValueError("suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")
    def __str__(self):
        suit_str = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}[self.suit]
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(self.rank, str(self.rank))
        return f"{rank_str}{suit_str}"

print(Card("S", 1))
print(Card("H", 11))
print(Card(rank=3, suit="C"))
print(Card("C", 1))


