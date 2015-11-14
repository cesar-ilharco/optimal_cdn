import heapq

from placement import PlacementManager


def placement(clients, servers):
	placement_manager = PlacementManager(servers)
	clients.sort(reverse=True)
	for client in clients:
		server = heapq.heappop(servers)
		placement_manager.place_client(client, server)
		heapq.heappush(servers, server)
	return placement_manager


def optimal_placement (placement_manager):
	avg_used_capacity = sum(server.used_capacity for server in placement_manager.servers) / len(placement_manager.servers)
	sorted_servers = sorted(placement_manager.servers)
	indexes = []
	max_used_capacity = sorted_servers[-1].used_capacity
	index, next_server = __find_closest_used_capacity(sorted_servers, avg_used_capacity)
	del sorted_servers[index]
	indexes.append(next_server.id)
	accumulated_capacity = avg_used_capacity + next_server.used_capacity - max_used_capacity
	lambda1 = accumulated_capacity/next_server.used_capacity
	placement_manager.set_multiplicative_factor(next_server, placement_manager.get_clients_served_by(next_server), lambda1)
	lambda2 = 1.0 - lambda1
	last_server = next_server
	for count in range(1, len(placement_manager.servers)):
		target = (count+2)*avg_used_capacity - max_used_capacity - accumulated_capacity
		index, next_server = __find_closest_used_capacity(sorted_servers, target)
		del sorted_servers[index]
		indexes.append(next_server.id)
		accumulated_capacity += next_server.used_capacity
		lambda1 = (accumulated_capacity-count*avg_used_capacity)/next_server.used_capacity
		placement_manager.set_multiplicative_factor(next_server, placement_manager.get_clients_served_by(next_server), lambda1)
		placement_manager.set_multiplicative_factor(last_server, placement_manager.get_clients_served_by(next_server), 1.0 - lambda1)
		last_server = next_server
	placement_manager.set_multiplicative_factor(last_server, placement_manager.get_clients_served_by(next_server), lambda2)
	return placement_manager, indexes


def __find_closest_used_capacity (servers, target):
	if len(servers) == 1:
		return [0, servers[0]]
	if target > servers[-1].used_capacity:
		return [len(servers)-1, servers[-1]]
	len_med = int(len(servers)/2)
	closest = [len_med, servers[len_med]]
	if servers[len_med].used_capacity == target:
		return closest
	if servers[len_med].used_capacity > target:
		temp = __find_closest_used_capacity(servers[:len_med], target)
		if abs(temp[1].used_capacity - target) < closest[1].used_capacity - target:
			return temp
		return closest
	temp = __find_closest_used_capacity(servers[len_med+1:], target)
	temp[0] += len_med + 1
	if abs(temp[1].used_capacity - target) < target - closest[1].used_capacity:
		return temp
	return closest
