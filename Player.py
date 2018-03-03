import random

class Player:

	def __init__(self, name, clientsocket):
		self.name = name
		self.clientsocket = clientsocket
		self.game = None
		self.deck = ["Copper"]*7 + ["Estate"]*3
		self.discard = []
		self.hand = []
		self.played = []
		self.action_count = 1
		self.buy_count = 1
		self.coin_count = 1

		random.shuffle(self.deck)
		self.draw(5)

	def send(self, packet):
		self.clientsocket.send(packet)

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

	def validate(self, options):
		while True:
			recv = self.clientsocket.recv(1024)
			if recv in options:
				return recv
			else:
				self.clientsocket.send("That option is not valid")

	def move(self, from_pile, to_pile, min_count, max_count):
		if max_count == 0:
			return
		else:
			if min_count == 0:
				self.send("You may choose a card")
				self.send("{}, or [Stop Choosing]".format(from_pile))
				choice = self.validate(from_pile + ["Stop Choosing"])
			else:
				self.send("Choose a card")
				self.send("{}".format(from_pile))
				choice = self.validate(from_pile)
			if choice == "Stop Choosing":
				return
			else:
				from_pile.remove(choice)
				to_pile.append(choice)
				return self.move(max(0, min_count - 1), max_count - 1)

	def action(self, card):
		if card is "Cellar":
			self.add_action(1)
			self.discard()
		elif card is "Chapel":
			self.move(self.hand, self.game.trash, 0, 4)
		elif card is "Moat":
			self.draw(2)
		elif card is "Harbinger":
			self.draw(1)
			self.add_action(1)
			self.move(self.discard, self.deck, 0, 1)
		elif card is "Merchant":
			self.draw(1)
			self.add_action(1)
		elif card is "Vassal":
			self.add_coin(2)
			card = self.deck.pop()
			self.discard.append(card)
			if self.discard[-1] in self.game.actions:
				self.clientsocket.send("You may play this card.")
				self.clientsocket.send("[Yes, No]")
				choice = self.validate(["Yes", "No"])
				if choice == "Yes":
					self.action(card)
				else:
					return
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
					pass
		elif card is "Gardens":
			pass
		elif card is "Militia":
			self.add_coin(2)
		elif card is "Moneylender":
			try:
				self.hand.remove(self.hand.index("Copper"))
				self.game.trash.append("Copper")
				self.add_coin(3)
			except:
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
			self.board["Gold"] -= 1
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
			for player in self.game.players:
				if players is not self:
					player.draw(1)
		elif card is "Festival":
			self.add_action(2)
			self.add_buy(1)
			self.add_coin(2)
		elif card is "Laboratory":
			self.draw(2)
			self.add_action(1)
		elif card is "Library":
			while len(self.hand) is not 7:
				self.draw(1)
				if self.hand[-1] in self.game.actions:
					#prompt to discard action card
					self.discard.append(self.hand.pop())
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
			for player in self.game.players:
				if player is not self:
					player.discard.append("Curse")
		elif card is "Artisan":
			pass
		self.played.append(card)

	def buy(self, card):
		if self.buy_count > 0:
			self.coin_count += self.hand.count("Copper") + self.hand.count("Silver")*2 + self.hand.count("Gold")*3
			if self.coin_count >= self.game.card_cost[card] and self.game.board[card] is not 0:
				self.game.board[card] -= 1
				self.discard.append(card)
				self.coin_count -= self.game.card_cost[card]
				self.buy_count -= 1