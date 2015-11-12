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


def optimal_placement_limited_capacity (placement_manager):
	C = sum(server.used_capacity for server in placement_manager.servers)
	C /= len(placement_manager.servers)
	sortedServers = sorted(placement_manager.servers)

	indexes = []
	C_max = sortedServers[-1].used_capacity
	closest = findClosestUsedCapacity(sortedServers, C)
	del sortedServers[closest[0]]
	indexes.append(closest[1].id)
	S = C + closest[1].used_capacity - C_max
	placement_manager.change_multiplicative_factor(closest[1], 0, S/closest[1].used_capacity)
	lambda2 = 1 - S/closest[1].used_capacity
	last_server = closest[1]
	count = 1
	while count < len(servers):
		var = (count+2)*C - C_max - S
		closest = findClosestUsedCapacity(sortedServers, var)
		del sortedServers[closest[0]]
		indexes.append(closest[1].id)
		S += closest[1].used_capacity
		placement_manager.change_multiplicative_factor(closest[1], 0, (S-count*C)/closest[1].used_capacity)
		placement_manager.change_multiplicative_factor(last_server, 1, 1 - (S-count*C)/closest[1].used_capacity)
		last_server = closest[1]
		count += 1
	placement_manager.change_multiplicative_factor(closest[1], 1, lambda2)
	return placement_manager, indexes


def findClosestUsedCapacity (array, target):
	if len(array) == 1:
		return [0, array[0]]
	if target > array[-1].used_capacity:
		return [len(array)-1, array[-1]]
	lenMed = int(len(array)/2)
	closest = [lenMed, array[lenMed]]
	if array[lenMed].used_capacity == target:
		return closest
	if array[lenMed].used_capacity > target:
		temp = findClosestUsedCapacity(array[:lenMed], target)
		if abs(temp[1].used_capacity - target) < closest[1].used_capacity - target:
			return temp
		return closest
	temp = findClosestUsedCapacity(array[lenMed+1:], target)
	temp[0] += lenMed + 1
	if abs(temp[1].used_capacity - target) < target - closest[1].used_capacity:
		return temp
	return closest
