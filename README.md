# optimal_cdn

Optimal algorithm to allocate client demands in a Content Delivery Network on the minimum possible number of servers of a given capacity, in two stages.

The solution satisfies the following constraints imposed by this telecommunications application:

(i) All client demands are fully satisfied at the end of the second stage of allocation;
(ii) For all clients whose demand is allocated at a given server on a given stage, the proportion of the demand allocated is the same.

The time complexity of the algorithm is O(N ln N), where N is the number of client demands.
