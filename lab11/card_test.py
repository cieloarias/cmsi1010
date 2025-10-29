import pytest
from card import Card


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