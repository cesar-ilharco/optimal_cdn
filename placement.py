class PlacementManager(object):

	def __init__ (self, servers_):
		self.servers = servers_
		self.__map_client_server = {}
		self.__map_server_clients = {server : set() for server in self.servers}

	def place_client(self, client, server):
		server.used_capacity += client.demand
		self.__map_client_server[client] = server
		self.__map_server_clients[server].add(client)

	def get_clients_served_by(self, server):
		return self.__map_server_clients[server]

	def get_server(self, client):
		return self.__map_client_server[client]

	def change_multiplicative_factor(self, server, number, multiplicative_factor):
		server.multiplicative_factors[number] = multiplicative_factor
