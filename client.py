class Client(object):

	def __init__ (self, id_, demand_):
		self.id = id_
		self.demand = demand_

	def __cmp__ (self, other):
		return cmp(self.demand, other.demand)


class ClientManager(object):

	def __init__(self):
		self.__latest_id = 0

	def create_client(self, demand):
		self.__latest_id += 1
		return Client(self.__latest_id, demand)
