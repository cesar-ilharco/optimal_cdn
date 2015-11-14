class Server(object):

	def __init__ (self, id_):
		self.id = id_
		self.used_capacity = 0.0

	def __lt__ (self, other):
		return self.used_capacity < other.used_capacity

class ServerManager(object):

	def __init__ (self):
		self.__latest_id = 0

	def create_server(self):
		self.__latest_id += 1
		return Server(self.__latest_id)

