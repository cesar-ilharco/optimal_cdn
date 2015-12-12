# optimal_cdn

Optimal algorithm to allocate client demands in a Content Delivery Network in the minimum possible number of servers of a given capacity, in two stages.

The solution satisfies the following constraints imposed by this telecommunications application:

(i) All client demands are fully satisfied at the end of the second stage of allocation;
(ii) The proportion of each client demand allocated in a given server at a given stage are equal, for all clients whose demand is allocated in this server at this stage.

The time complexity of the algorithm is O(N ln N), where N is the number of client demands.
