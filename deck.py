import random
from card import Card

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Deck:

	def __init__(self):
		#shuffle deck of cards on initialisation
		self.deck = []
		for suit in suits:
			for rank in ranks:
				card = Card(suit, rank)
				self.deck.append(card)


	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp = "\n"+card.__str__()
		return deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()
