class Server(object):

	def __init__ (self, id_, capacity_limit_):
		self.id = id_
		self.capacity_limit = capacity_limit_
		self.used_capacity = 0

class ServerManager(object):

	def __init__ (self):
		self.__latest_id = 0

	def create_server(self, capacity_limit = None):
		self.__latest_id += 1
		return Server(self.__latest_id, capacity_limit)

