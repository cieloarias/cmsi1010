import pytest
from cards import (
    Card, standard_deck, shuffled_deck, deal_one_five_card_hand,
    deal, poker_classification)


def make_card(description):
    if len(description) != 2:
        return None
    rank_str = description[:-1]
    suit_str = description[-1].upper()
    if suit_str not in "SHDC" or rank_str not in "A23456789TJQK":
        return None
    return Card(suit=suit_str, rank="A23456789TJQK".index(rank_str) + 1)


def make_hand(description):
    return {make_card(card) for card in description.split()}


def test_valid_cards():
    assert str(Card(suit="H", rank=10)) == "10♥"
    assert str(Card(suit="S", rank=1)) == "A♠"
    assert str(Card(suit="D", rank=11)) == "J♦"
    assert str(Card(suit="C", rank=12)) == "Q♣"
    assert str(Card(suit="H", rank=13)) == "K♥"
    assert str(Card(suit="S", rank=5)) == "5♠"
    assert str(Card(suit="D", rank=3)) == "3♦"
    assert str(Card(suit="C", rank=2)) == "2♣"


def test_invalid_suit():
    with pytest.raises(ValueError):
        Card(suit="X", rank=5)
    with pytest.raises(ValueError):
        Card(suit="SPADES", rank=10)


def test_invalid_rank():
    with pytest.raises(ValueError):
        Card(suit="S", rank=14)
    with pytest.raises(ValueError):
        Card(suit="D", rank=0)
    with pytest.raises(ValueError):
        Card(suit="D", rank=3.5)
    with pytest.raises(ValueError):
        Card(suit="D", rank="10")


def test_cards_are_truly_immutable():
    card = Card(suit="H", rank=10)
    with pytest.raises(AttributeError):
        card.suit = "S"
    with pytest.raises(AttributeError):
        card.rank = 5
    with pytest.raises(AttributeError):
        card.dog = "dog"


def test_standard_deck():
    deck = standard_deck()
    assert isinstance(deck, list)
    assert len(deck) == 52
    assert all(isinstance(card, Card) for card in deck) is True
    deck_as_string = ''.join(str(card) for card in deck)
    assert deck_as_string == (
        "A♠2♠3♠4♠5♠6♠7♠8♠9♠10♠J♠Q♠K♠"
        "A♥2♥3♥4♥5♥6♥7♥8♥9♥10♥J♥Q♥K♥"
        "A♦2♦3♦4♦5♦6♦7♦8♦9♦10♦J♦Q♦K♦"
        "A♣2♣3♣4♣5♣6♣7♣8♣9♣10♣J♣Q♣K♣"
    )


def test_shuffled_deck():
    deck = standard_deck()
    assert isinstance(deck, list)
    assert len(deck) == 52
    shuffled = shuffled_deck()
    assert isinstance(shuffled, list)
    assert len(shuffled) == 52
    for suit in "SHDC":
        for rank in range(1, 14):
            assert Card(suit, rank) in shuffled


def test_deal_one_five_card_hand():
    hand = deal_one_five_card_hand()
    assert isinstance(hand, set)
    assert len(hand) == 5
    assert all(isinstance(card, Card) for card in hand)


def test_deal_invalid_inputs():
    with pytest.raises(TypeError):
        # Illegal number of hands
        deal("two", 5)
    with pytest.raises(TypeError):
        # Illegal cards per hand
        deal(2, "five")
    with pytest.raises(ValueError):
        # Number of hands too small
        deal(0, 5)
    with pytest.raises(ValueError):
        # Cards per hand too small
        deal(2, -5)
    with pytest.raises(ValueError):
        # Not enough cards in the deck
        deal(11, 5)


def test_deal_valid_inputs():
    hands = deal(6, 7)
    assert isinstance(hands, list)
    assert len(hands) == 6
    for hand in hands:
        assert isinstance(hand, set)
        assert len(hand) == 7
        assert all(isinstance(card, Card) for card in hand)
    # Check that all cards are unique across both hands
    all_cards = set().union(*hands)
    assert len(all_cards) == 42


def test_poker_classification():
    tests = [
        (make_hand("2H 3H 4H 5H 6H"), "Straight Flush"),
        (make_hand("JH TH QH KH AH"), "Royal Flush"),
        (make_hand("QS TS AS KS JS"), "Royal Flush"),
        (make_hand("2H 2D 3H 3D 4H"), "Two Pair"),
        (make_hand("KD 2D 3H 3D KH"), "Two Pair"),
        (make_hand("2H 2D 2C 3H 4H"), "Three of a Kind"),
        (make_hand("2S 3H 4H 5H 7H"), "High Card"),
        (make_hand("2S 3H 4H 5H KH"), "High Card"),
        (make_hand("2H 3H 4H 5H 6D"), "Straight"),
        (make_hand("2H 3H 4H 5H AD"), "Straight"),
        (make_hand("KH QC JC TC AD"), "Straight"),
        (make_hand("2C TC 4C 5C 6C"), "Flush"),
        (make_hand("2H 2D 2C 2S 3H"), "Four of a Kind"),
        (make_hand("2H AD AC AS AH"), "Four of a Kind"),
    ]
    for hand, expected in tests:
        assert poker_classification(hand) == expected