import unittest
import random

from server import ServerManager


class TestServerManager(unittest.TestCase):

	def test_create_servers(self):
		number_servers = 30
		server_manager = ServerManager()
		servers = [server_manager.create_server() for i in range(number_servers)]
		for i in range(number_servers):
			self.assertEqual(servers[i].id, i+1)


if __name__ == '__main__':
    unittest.main()