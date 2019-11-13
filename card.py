class Card:

	def __init__(self, suit, rank):
		#This may just require getting the next card from the Deck class which is shuffled on initialisation
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return "This card is the {} of {}".format(self.rank, self.suit)
