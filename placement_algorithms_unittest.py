import unittest

from client import ClientManager
from server import ServerManager
from placement_algorithms import placement, optimal_placement

class TestPlacementAlgorithms(unittest.TestCase):

	def __test_placement(self, clients, servers, optimal_usages):
		placement_manager = placement(clients, servers)
		(clients, servers)
		used_capacities = sorted([server.used_capacity for server in servers])
		self.assertEqual(used_capacities, optimal_usages)

	def __test_optimal_placement(self, clients, servers):
		placement_manager = optimal_placement(clients, servers)
		avg_used_capacity = sum(client.demand for client in clients) / len(servers)
		for server in servers:
			self.assertTrue(abs(server.used_capacity - avg_used_capacity) < 10**(-5))
			for client in clients:
			for server in placement_manager.get_servers(client):
				self.assertTrue(placement_manager.get_multiplicative_factor_from_client(client, server) >= -10**(-5))
			self.assertEqual(sum(placement_manager.get_multiplicative_factor_from_client(client, server) for server in placement_manager.get_servers(client)), 1)
	
	def __get_clients_and_servers(self, demands, number_servers):
		client_manager = ClientManager()
		server_manager = ServerManager()
		clients = [client_manager.create_client(demand) for demand in demands]
		servers = [server_manager.create_server() for i in range(number_servers)]
		return (clients, servers)

	def test_placement_1(self):
		demands = [11, 8, 9, 15, 5, 3, 12, 7]
		number_servers = 4
		clients, servers = self.__get_clients_and_servers(demands, number_servers)
		optimal_usages = [17, 17, 18, 18]
		self.__test_placement(clients, servers, optimal_usages)

	def test_placement_2(self):
		demands = [7, 5, 18, 13, 8, 21, 6, 14]
		number_servers = 3
		clients, servers = self.__get_clients_and_servers(demands, number_servers)
		optimal_usages = [28, 32, 32]
		self.__test_placement(clients, servers, optimal_usages)

	def test_placement_3(self):
		demands = [24, 9, 1, 13, 7, 8, 4]
		number_servers = 3
		clients, servers = self.__get_clients_and_servers(demands, number_servers)
		optimal_usages = [21, 21, 24]
		self.__test_placement(clients, servers, optimal_usages)

	def test_placement_4(self):
		demands = [12, 4] + [10]*142
		number_servers = 100
		clients, servers = self.__get_clients_and_servers(demands, number_servers)
		optimal_usages = [10]*55 + [12, 14] + [20]*43
		self.__test_placement(clients, servers, optimal_usages)

	def test_placement_5(self):
		demands = range(1,100)
		number_servers = 115
		clients, servers = self.__get_clients_and_servers(demands, number_servers)
		optimal_usages = [0]*15 + list(range(100))
		self.__test_placement(clients, servers, optimal_usages)

	def test_placement_6(self):
		demands = [10] * 1000
		number_servers = 50
		clients, servers = self.__get_clients_and_servers(demands, number_servers)
		optimal_usages = [200] * 50
		self.__test_placement(clients, servers, optimal_usages)

	def test_optimal_placement_1(self):
		demands = [11, 8, 9, 15, 5, 3, 12, 7]
		number_servers = 4
		clients, servers = self.__get_clients_and_servers(demands, number_servers)
		self.__test_optimal_placement(clients, servers)

	def test_optimal_placement_2(self):
		demands = [7, 5, 18, 13, 8, 21, 6, 14]
		number_servers = 3
		clients, servers = self.__get_clients_and_servers(demands, number_servers)
		self.__test_optimal_placement(clients, servers)

	def test_optimal_placement_3(self):
		demands = [24, 9, 1, 13, 7, 8, 4]
		number_servers = 3
		clients, servers = self.__get_clients_and_servers(demands, number_servers)
		self.__test_optimal_placement(clients, servers)

	def test_optimal_placement_4(self):
		demands = [12, 4] + [10]*142
		number_servers = 100
		clients, servers = self.__get_clients_and_servers(demands, number_servers)
		self.__test_optimal_placement(clients, servers)

	def test_optimal_placement_5(self):
		demands = [5, 3, 6, 23, 6, 34, 21, 15, 31, 17, 15, 4, 6, 11]
		number_servers = 4
		clients, servers = self.__get_clients_and_servers(demands, number_servers)
		self.__test_optimal_placement(clients, servers)

	def test_optimal_placement_6(self):
		demands = [10] * 1000
		number_servers = 50
		clients, servers = self.__get_clients_and_servers(demands, number_servers)
		self.__test_optimal_placement(clients, servers)



if __name__ == '__main__':
    unittest.main()
