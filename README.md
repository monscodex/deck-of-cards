# deck-of-cards
Simple and clean python implementation of a deck of cards.
## How to use it?
### Card
**Suit**, **Rank** and **Card** classes are defined in `card.py`

You can use them as follows:
```python
six_of_spades = Card(rank=Rank.SIX, suit=Suit.SPADES)
ace_of_hearts = Card(rank=Rank.ACE, suit=Suit.HEARTS)

print(six_of_spades < ace_of_hearts) # False
```

### Deck
The deck is implemented as **DeckOfCards** and defined in `deck.py`

Here's an example:

Create the deck
```python
deck = DeckOfCards()

print(deck)
# [
#     Card(rank=<Rank.ACE: 1>, suit=<Suit.SPADES: 1>),
#     Card(rank=<Rank.TWO: 2>, suit=<Suit.SPADES: 1>),
#     ...
# ]
```

Mix the deck
```python
deck.mix()

print(deck)
# [
#     Card(rank=<Rank.FIVE: 5>, suit=<Suit.SPADES: 1>),
#     Card(rank=<Rank.TEN: 10>, suit=<Suit.CLUBS: 2>),
#     ...
# ]
```

Distribute the cards
```python
per_player_cards, undistributed_cards = deck.distribute(number_of_payers=15)

print(per_player_cards)
# [
#     [
#         Card(rank=<Rank.FIVE: 5>, suit=<Suit.SPADES: 1>),
#         Card(rank=<Rank.THREE: 3>, suit=<Suit.CLUBS: 2>),
#         Card(rank=<Rank.QUEEN: 12>, suit=<Suit.SPADES: 1>)
#     ],
#     [
#         Card(rank=<Rank.TEN: 10>, suit=<Suit.CLUBS: 2>),
#         Card(rank=<Rank.TWO: 2>, suit=<Suit.SPADES: 1>),
#         Card(rank=<Rank.QUEEN: 12>, suit=<Suit.DIAMONDS: 4>)
#     ],
#     ...
# ]

print(undistributed_cards)
# [
#     Card(rank=<Rank.TEN: 10>, suit=<Suit.SPADES: 1>),
#     Card(rank=<Rank.EIGHT: 8>, suit=<Suit.DIAMONDS: 4>),
#     Card(rank=<Rank.SIX: 6>, suit=<Suit.SPADES: 1>),
#     ...
# ]
```

## Developer's note
Enjoy the code!

Have a good day, monscodex
