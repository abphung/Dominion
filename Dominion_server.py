import socket
import thread
from player import Player
from game import Game

class Dominion_server:

	def __init__(self):
		self.s = socket.socket()
		self.host = socket.gethostname()
		self.port = 50000

		self.s.bind((host, port))
		self.s.listen(5)
		while True:
			c, addr = s.accept()
			thread.start_new_thread(self.on_new_client, (c, addr))

	def on_new_client(self, clientsocket, addr):
		name = clientsocket.recv(1024)
		player = Player(name, clientsocket)
		self.players.append(player)
		self.queue.append(player)
		if len(self.queue) >= 2:
			player1 = self.queue.pop()
			player1.clientsocket.send("Found a worth opponent!")
			player2 = self.queue.pop()
			player2.clientsocket.send("Found a worth opponent!")
			#TODO games with more than 2 players
			self.games.append(Game(player1, player2))
		else:
			clientsocket.send("Searching for an opponent!")


