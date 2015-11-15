class PlacementManager(object):

	def __init__ (self, servers_):
		self.servers = servers_
		self.__map_client_servers = dict()
		self.__map_server_clients = {server : {} for server in self.servers}

	def place_client(self, client, server):
		server.used_capacity += client.demand
		self.__map_client_servers[client] = {server : 1.0}
		self.__map_server_clients[server][client] = 1.0

	def get_clients_served_by(self, server):
		return self.__map_server_clients[server]

	def get_servers(self, client):
		return self.__map_client_servers[client]

	def set_multiplicative_factor(self, server, clients, multiplicative_factor):
		for client in clients:
			if client not in self.__map_client_servers:
				self.place_client(client, server)
			self.__map_client_servers[client][server] = multiplicative_factor
			self.__map_server_clients[server][client] = multiplicative_factor

