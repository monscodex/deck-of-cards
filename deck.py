from random import randint
from card import Card, Suit, Rank


def main():
    deck = DeckOfCards()

    print(f"\tFIRST 3 INITIAL CARDS: {deck.cards[:3]}\n")

    deck.mix()

    print(f"\tFIRST 3 MIXED CARDS: {deck.cards[:3]}\n")

    # Distribute the cards to 15 players
    per_player_cards, undistributed_cards = deck.distribute(number_of_payers=15)

    print(
        f"\tFIRST 2 PLAYER CARDS: {per_player_cards[:2]}\n\tUNDISTRIBUTED CARDS: {undistributed_cards}"
    )


class DeckOfCards:
    def __init__(self, suits=None, ranks=None):
        self.suits = list(Suit) if not suits else suits
        self.ranks = list(Rank) if not ranks else ranks

        self.cards = self.get_new_deck()

    def get_new_deck(self) -> list[Card]:
        return [
            Card(suit=suit, rank=rank) for suit in self.suits for rank in self.ranks
        ]

    def mix(self) -> None:
        mixed_deck = []

        for card in self.cards:
            self._insert_card_in_random_place(card, mixed_deck)

        self.cards = mixed_deck

    def _insert_card_in_random_place(self, card: Card, cards: list[Card]) -> None:
        # Include next index after the last card in the deck
        random_index = randint(0, len(cards))

        cards.insert(random_index, card)

    def distribute(self, number_of_payers: int) -> tuple[list[list[Card]], list[Card]]:
        """
        Returns:
            - A list of the list of cards per player for all the players.
            - A list of undistributed cards
        Cards are distributed giving one card per player until everyone has the same number of cards and there aren't enough cards to give one more to everybody.
        """
        number_cards_to_distribute = self._get_number_cards_to_distribute(
            number_of_payers
        )

        per_player_cards = [
            self.cards[player_index:number_cards_to_distribute:number_of_payers]
            for player_index in range(number_of_payers)
        ]

        undistributed_cards = self.cards[number_cards_to_distribute:]

        return per_player_cards, undistributed_cards

    def _get_number_cards_to_distribute(self, number_of_players: int) -> int:
        number_undistributed_cards = len(self.cards) % number_of_players
        number_cards_to_distribute = len(self.cards) - number_undistributed_cards

        return number_cards_to_distribute

    def __repr__(self) -> str:
        return repr(self.cards)


if __name__ == "__main__":
    main()
