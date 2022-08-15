#Dt.20.02.2021
#Dev.: Sourin Biswas
#Topic: Deck of 52 Cards
import random

class Card:
	def __init__(self, suit, value):
		self.suit=suit
		self.value=value

	def show(self):
		print("A {} of {} appeared!".format(self.suit, self.value))

class Deck:
	def __init__(self):
		self.cards=[]
		self.build()

	def build(self):
		for s in ["Spades", "Diamonds", "Clubs", "Hearts"]:
			for v in ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Face Card", "Face Card", "Face Card"]:
				self.cards.append(Card(s,v))

	def show(self):
		for c in self.cards:
			c.show()

class Player:
	def __init__(self):
		pass

deck=Deck()
deck.show()