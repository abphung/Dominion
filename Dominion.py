import random
import socket

class Game:

	def __init__(self):
		self.players = []
		self.trash = []
		self.card_cost = {
				"Copper": 0,
				"Curse": 0,
				"Estate": 2,
				"Silver": 3,
				"Duchy": 5,
				"Gold": 6,
				"Province": 8,

				"Cellar": 2,
				"Chapel": 2,
				"Moat": 2,
				"Harbinger": 3,
				"Merchant": 3,
				"Vassal": 3,
				"Village":3,
				"Workshop": 3,
				"Bureaucrat": 4,
				"Gardens": 4,
				"Militia": 4,
				"Moneylender": 4,
				"Poacher": 4,
				"Remodel": 4,
				"Smithy": 4,
				"Throne Room": 4,
				"Bandit": 5,
				"Council Room": 5,
				"Festival": 5,
				"Laboratory": 5,
				"Library": 5,
				"Market": 5,
				"Mine": 5,
				"Sentry": 5,
				"Witch": 5,
				"Artisan": 6
		}


		p1 = Player("Awesome Andrew", self)
		p2 = Player("Retard Rebecca", self)
		print p1.hand
		print p2.hand

class Player:

	def __init__(self, name, game):
		self.name = name
		self.game = game
		game.players.append(self)
		self.deck = ["Copper"]*7 + ["Estate"]*3
		self.discard = []
		self.hand = []
		self.played = []

		random.shuffle(self.deck)
		self.draw(5)

	def draw(self, count):
		for i in range(count):
			if self.deck is []:
				random.shuffle(self.discard)
				self.deck = self.discard
				self.discard = []
			self.hand.append(self.deck.pop())


	def add_action(self, count):
		self.action_count += count

	def add_buy(self, count):
		self.buy_count += count

	def add_coin(self, count):
		self.coin_count += count

	def trash(self, count):
		pass

	def discard(self, count):
		pass



	def action(self, card):
		if card is "Cellar":
			self.add_action(1)
			self.discard()
		elif card is "Chapel":
			self.game.trash()
		elif card is "Moat":
			self.draw(2)
		elif card is "Harbinger":
			self.draw(1)
			self.add_action(1)
			#kahng will deal with this
			print self.discard
			self.deck.append(self.discard.pop())
		elif card is "Merchant":
			self.draw(1)
			self.add_action(1)
		elif card is "Vassal":
			self.add_coin(2)
			self.discard.append(self.deck.pop())
			if self.discard[-1] is in self.game.actions:
				pass
				#ask player if they want to play or not
		elif card is "Village":
			self.draw(1)
			self.add_action(2)
		elif card is "Workshop":
			pass
		elif card is "Bureaucrat":
			self.deck.append("Silver")
			for player in self.game.players:
				if player is not self:
					#ask players which victory card to show
		elif card is "Gardens":
			pass
		elif card is "Militia":
			self.add_coin(2)
		elif card is "Moneylender":
			pass
		elif card is "Poacher":
			self.draw(1)
			self.add_action(1)
			self.add_coin(1)
		elif card is "Remodel":
			pass
		elif card is "Smithy":
			self.draw(3)
		elif card is "Throne Room":
			pass
		elif card is "Bandit":
			self.discard.append("Gold")
			for player in self.game.players:
				if player is not self:
					for i in range(2):
						player.draw(1)
						if player.hand[-1] is "Gold" or player.hand[-1] is "Silver":
							self.game.trash.append(player.hand.pop())
						else:
							player.discard.append(player.hand.pop())
		elif card is "Council Room":
			self.draw(4)
			self.add_buy(1)
		elif card is "Festival":
			self.add_action(2)
			self.add_buy(1)
			self.add_coin(2)
		elif card is "Laboratory":
			self.draw(2)
			self.add_action(1)
		elif card is "Library":
			pass
		elif card is "Market":
			self.draw(1)
			self.add_action(1)
			self.add_buy(1)
			self.add_coin(1)
		elif card is "Mine":
			pass
		elif card is "Sentry":
			self.draw(1)
			self.add_action(1)
		elif card is "Witch":
			self.draw(2)
		elif card is "Artisan":
			pass
		self.played.append(card)


if __name__ == '__main__':
	game = Game()
