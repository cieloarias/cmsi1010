from dataclasses import dataclass
from random import shuffle
from collections import Counter


@dataclass(frozen=True)
class Card:
    suit: str
    rank: int

    def __post_init__(self):
        if self.suit not in ("S", "H", "D", "C"):
            raise ValueError("suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")

    def __str__(self):
        suit_str = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}[self.suit]
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(
            self.rank, str(self.rank))
        return f"{rank_str}{suit_str}"


def standard_deck():
    return [Card(suit, rank) for suit in "SHDC" for rank in range(1, 14)]


def shuffled_deck():
    cards = standard_deck()
    shuffle(cards)
    return cards


def deal_one_five_card_hand():
    deck = shuffled_deck()
    return set(deck[:5])


def deal(number_of_hands, cards_per_hand):
    """
    Return a list of sets, each representing one hand of cards.

    - number_of_hands: how many players
    - cards_per_hand: how many cards per player
    """
    
    if not isinstance(number_of_hands, int) or not isinstance(cards_per_hand, int):
        raise TypeError("Both number_of_hands and cards_per_hand must be integers.")

    if number_of_hands <= 0 or cards_per_hand <= 0:
        raise ValueError("Both numbers must be positive.")

    if number_of_hands * cards_per_hand > 52:
        raise ValueError("Not enough cards in a deck for that many hands.")

    # Shuffle a new deck
    deck = shuffled_deck()

    # Deal hands by slicing the deck
    hands = []
    for i in range(number_of_hands):
        hand = set(deck[i*cards_per_hand : (i+1)*cards_per_hand])
        hands.append(hand)

    return hands

def poker_classification(hand):
    if not isinstance(hand,set):
        raise TypeError("Hand must be a set of 5 cards.")
    if len(hand)!=5:
        raise ValueError("Hand must contain exactly 5 cards.")
    if not all(hasattr(card,"rank") and hasattr(card,"suit") for card in hand):
        raise TypeError("All elements in hand must be Card objects.")

    ranks=[card.rank for card in hand]
    suits=[card.suit for card in hand]
    rank_counts=Counter(ranks)
    counts=sorted(rank_counts.values(),reverse=True)
    is_flush=len(set(suits))==1
    ranks_sorted=sorted([14 if r==1 else r for r in ranks])
    is_straight=len(set(ranks_sorted))==5 and ranks_sorted[-1]-ranks_sorted[0]==4
    if set(ranks)=={1,2,3,4,5}:
        is_straight=True
    patterns=[
        (is_straight and is_flush and set(ranks_sorted)=={10,11,12,13,14},"Royal Flush"),
        (is_straight and is_flush,"Straight Flush"),
        (counts==[4,1],"Four of a Kind"),
        (counts==[3,2],"Full House"),
        (is_flush,"Flush"),
        (is_straight,"Straight"),
        (counts==[3,1,1],"Three of a Kind"),
        (counts==[2,2,1],"Two Pair"),
        (counts==[2,1,1,1],"One Pair"),
    ]
    for cond,name in patterns:
        if cond:
            return name
    return "High Card"