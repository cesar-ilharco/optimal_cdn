import unittest
import random

from server import ServerManager


class TestServerManager(unittest.TestCase):

	def test_create_servers_unlimited_capacity(self):
		number_servers = 30
		server_manager = ServerManager()
		servers = [server_manager.create_server() for i in range(number_servers)]
		for i in range(number_servers):
			self.assertEqual(servers[i].id, i+1)
			self.assertIs(servers[i].capacity_limit, None)

	def test_create_servers_limited_capacity(self):
		number_servers = 30
		capacity_limits = [random.randint(100, 1000) for i in range(number_servers)]
		server_manager = ServerManager()
		servers = [server_manager.create_server(limit) for limit in capacity_limits]
		for i in range(number_servers):
			self.assertEqual(servers[i].id, i+1)
			self.assertEqual(servers[i].capacity_limit, capacity_limits[i])


if __name__ == '__main__':
    unittest.main()