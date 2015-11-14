import unittest
import random

from placement import PlacementManager
from server import ServerManager
from client import ClientManager


class TestPlacementManager(unittest.TestCase):

	def test_place_and_get_zero_clients(self):
		server_manager = ServerManager()
		servers = [server_manager.create_server() for i in range(30)]
		placement_manager = PlacementManager(servers)
		for server in servers:
			self.assertEquals(placement_manager.get_clients_served_by(server), {})

	def test_place_in_single_server(self):
		server_manager = ServerManager()
		client_manager = ClientManager()
		server = server_manager.create_server()
		clients = [client_manager.create_client(random.randint(10,30)) for i in range(100)]
		placement_manager = PlacementManager([server])
		for client in clients:
			placement_manager.place_client(client, server)
		for client in clients:
			self.assertEquals(placement_manager.get_servers(client), {server : 1.0})
		self.assertEquals(placement_manager.get_clients_served_by(server), {client : 1.0 for client in clients})
	
	def test_place_in_multiple_servers(self):
		number_servers = 30
		number_clients = 1000
		server_manager = ServerManager()
		client_manager = ClientManager()
		servers = [server_manager.create_server() for i in range(number_servers)]
		clients = [client_manager.create_client(random.randint(10,30)) for i in range(number_clients)]
		placement_manager = PlacementManager(servers)
		s = 0
		for client in clients:
			placement_manager.place_client(client, servers[s])
			s = (s+1)%number_servers
		for i in range(number_clients):
			self.assertEquals(placement_manager.get_servers(clients[i]), {servers[i%number_servers] : 1.0})
		for i in range(number_servers):
			served_clients = [clients[j] for j in range(i, number_clients, number_servers)]
			self.assertEquals(placement_manager.get_clients_served_by(servers[i]), {client : 1.0 for client in served_clients})
			self.assertEquals(servers[i].used_capacity, sum(client.demand for client in served_clients))

	def test_set_multiplicative_factors(self):
		number_servers = 2
		number_clients = 1000
		server_manager = ServerManager()
		client_manager = ClientManager()
		servers = [server_manager.create_server() for i in range(number_servers)]
		clients = [client_manager.create_client(random.randint(10,30)) for i in range(number_clients)]
		placement_manager = PlacementManager(servers)
		multiplicative_factors = [random.random() for i in range(number_clients)]
		s = 0
		for i in range(number_clients):
			placement_manager.set_multiplicative_factor(servers[0], clients[i:i+1], multiplicative_factors[i])
			placement_manager.set_multiplicative_factor(servers[1], clients[i:i+1], 1.0 - multiplicative_factors[i])
		for i in range(number_clients):
			retrieved_servers = placement_manager.get_servers(clients[i])
			self.assertEquals(retrieved_servers[servers[0]], multiplicative_factors[i])
			self.assertEquals(retrieved_servers[servers[1]], 1.0 - multiplicative_factors[i])
		retrieved_clients = placement_manager.get_clients_served_by(servers[0])
		self.assertEquals(retrieved_clients, {clients[i] : multiplicative_factors[i] for i in range(number_clients)})
		retrieved_clients = placement_manager.get_clients_served_by(servers[1])
		self.assertEquals(retrieved_clients, {clients[i] : 1.0 - multiplicative_factors[i] for i in range(number_clients)})


if __name__ == '__main__':
    unittest.main()