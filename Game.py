class Game:

	def __init__(self, player1, player2):
		self.players = [player1, player2]
		player1.game = self
		player2.game = self
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

		self.board = {}
		temp = self.actions + ["Gardens"]
		random.shuffle(temp)
		for card in temp[:10]:
			self.board[card] = 10
			#TODO number of cards is a function of players
		self.board["Copper"] = 20
		self.board["Silver"] = 20
		self.board["Gold"] = 20
		self.board["Curse"] = 20
		self.board["Estate"] = 20
		self.board["Duchy"] = 20
		self.board["Province"] = 20

		self.update()

	def update(self):
		while True:
			pass
			#Player1.clientsocket.recv(1024)