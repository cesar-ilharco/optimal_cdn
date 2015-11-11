import heapq

from placement import PlacementManager

def optimal_placement_unlimited_capacity(clients, servers):
	placement_manager = PlacementManager(servers)
	clients.sort(reverse=True)
	for client in clients:
		server = heapq.heappop(servers)
		placement_manager.place_client(client, server)
		heapq.heappush(servers, server)
	return placement_manager
