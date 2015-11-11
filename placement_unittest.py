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
			self.assertEquals(placement_manager.get_clients_served_by(server), set())

	def test_place_in_single_server(self):
		server_manager = ServerManager()
		client_manager = ClientManager()
		server = server_manager.create_server()
		clients = [client_manager.create_client(random.randint(10,30)) for i in range(100)]
		placement_manager = PlacementManager([server])
		for client in clients:
			placement_manager.place_client(client, server)
		for client in clients:
			self.assertIs(placement_manager.get_server(client), server)
		self.assertEquals(placement_manager.get_clients_served_by(server), set(clients))
	
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
			self.assertIs(placement_manager.get_server(clients[i]), servers[i%number_servers])
		for i in range(number_servers):
			served_clients = [clients[j] for j in range(i, number_clients, number_servers)]
			self.assertEquals(placement_manager.get_clients_served_by(servers[i]), set(served_clients))
			self.assertEquals(servers[i].used_capacity, sum(client.demand for client in served_clients))


if __name__ == '__main__':
    unittest.main()