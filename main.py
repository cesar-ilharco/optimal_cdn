from client import ClientManager
from server import ServerManager
from placement_algorithms import optimal_placement_unlimited_capacity

def read_input(file_name):
    f = file(file_name, 'r')
    client_manager = ClientManager()
    server_manager = ServerManager()
    if f.readline() == 'limited':
    	capacity_limits = map(int, f.readline().split())
    	servers = [server_manager.create_server(limit) for limit in capacity_limits]
    else:
    	number_servers = int(f.readline())
    	servers = [server_manager.create_server() for i in range(number_servers)]
    demands = map(int, f.readline().split())
    clients = [client_manager.create_client(demand) for demand in demands]
    return [clients, servers]

if __name__ == '__main__':
	clients, servers = read_input('input_1.txt')
	placement_manager = optimal_placement_unlimited_capacity(clients, servers)
	for server in servers:
		served_clients = placement_manager.get_clients_served_by(server)
		print "Server", server.id, ", used capacity =", server.used_capacity
		print "Client ids:", [client.id for client in served_clients]
		print "Client demands:", [client.demand for client in served_clients]
		print "########################################################################"




