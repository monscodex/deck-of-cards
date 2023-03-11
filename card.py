from enum import Enum, IntEnum
from dataclasses import dataclass, field

def main():
    print(f"Suits: {list(Suit)}")

    print(f"Ace < Queen: {Rank.ACE < Rank.QUEEN}")

    six_of_spades = Card(rank=Rank.SIX, suit=Suit.SPADES)
    ace_of_hearts = Card(rank=Rank.ACE, suit=Suit.HEARTS)
    print(f"Six of Spades < Ace of Hearts: {six_of_spades < ace_of_hearts}")

class Suit(Enum):
    SPADES = 1
    CLUBS = 2
    HEARTS = 3
    DIAMONDS = 4


# IntEnum provides order
class Rank(IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


@dataclass(order=True)
class Card:
    rank: Rank
    suit: Suit = field(compare=False)

if __name__ == "__main__":
    main()
