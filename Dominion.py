import random
import socket
import thread

def on_new_client(clientsocket,addr):
        while True:
            msg = clientsocket.recv(1024) 
            #do some checks and if msg == someWeirdSignal: break:
            print addr, ' >> ', msg
            msg = raw_input('SERVER >> ') 
            #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
            clientsocket.send(msg) 
        clientsocket.close()

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

		self.actions = [
				"Cellar",
				"Chapel",
				"Moat",
				"Harbinger",
				"Merchant",
				"Vassal",
				"Village",
				"Workshop",
				"Bureaucrat",
				"Militia",
				"Moneylender",
				"Poacher",
				"Remodel",
				"Smithy",
				"Throne Room",
				"Bandit",
				"Council Room",
				"Festival",
				"Laboratory",
				"Library",
				"Market",
				"Mine",
				"Sentry",
				"Witch",
				"Artisan"
		]

		self.attacks = [
				"Bureaucrat",
				"Militia",
				"Bandit",
				"Witch"
		]

		self.treasure = [
				"Copper"
				"Silver"
				"Gold"
		]

		self.victory = {
				"Estate": 1,
				"Duchy": 3,
				"Province": 6,
				"Curse": -1
		}

		self.board = {

		}

		temp = self.actions + ["Gardens"]
		random.shuffle(temp)
		for card in temp[:10]:
			self.board[card] = 10
			#TODO number of cards is a function of players
		self.board["Copper"] =
		self.board["Silver"] =
		self.board["Gold"] =
		self.board["Curse"] =
		self.board["Estate"] = 
		self.board["Duchy"] =
		self.board["Province"] =



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
		self.action_count = 1
		self.buy_count = 1
		self.coin_count = 1

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
			self.game.trash.append()
			#ask player which card to trash
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
			if self.discard[-1] in self.game.actions:
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
					pass
		elif card is "Gardens":
			pass
		elif card is "Militia":
			self.add_coin(2)
		elif card is "Moneylender":
			try:
				self.hand.remove(self.hand.index("Copper"))
				self.game.trash.append("Copper")
				self.add_coin(3);
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



if __name__ == '__main__':
	print "Welcome to Dominion!"
	print "Create a lobby(create) or join a lobby(join <ip address>)"
	while True:
		st = raw_input()
		if st == 'create':
			s = socket.socket()         # Create a socket object
			host = socket.gethostname() # Get local machine name
			port = 50000                # Reserve a port for your service.

			print 'Server started!'
			print 'Waiting for clients...'

			s.bind((host, port))        # Bind to the port
			s.listen(5)                 # Now wait for client connection.
			while True:
				c, addr = s.accept()     # Establish connection with client.
				print 'Got connection from', addr
				thread.start_new_thread(on_new_client,(c,addr))
			s.close()
		elif st.split(" ")[0] == 'join':
			s = socket.socket()
			host = socket.gethostname()
			port = 50000
			s.connect((host, port))
		else:
			print "Invalid Input"
			print st
			print st == 'create'
			print type(st)
			print len(st)
