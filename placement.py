class PlacementManager(object):

    """
    Manages client placement into servers.
    """

    def __init__(self, servers_):
        """
        Initialized from a list of servers and no clients.
        """
        self.servers = servers_
        self.__map_client_servers = dict()
        self.__map_server_clients = {server : {} for server in self.servers}

    def place_client(self, client, server):
        """
        Place a single client into a server.
        Update server's used_capacity and insert client into dictionaries.
        """
        server.used_capacity += client.demand
        self.__map_client_servers[client] = {server : 1.0}
        self.__map_server_clients[server][client] = 1.0

    def get_clients_served_by(self, server):
        return self.__map_server_clients[server]

    def get_servers(self, client):
        return self.__map_client_servers[client]

    def set_multiplicative_factor(self, server, clients, multiplicative_factor):
        """
        Change multiplicative_factor for a list of clients and a single host.
        Add clients into dictionaries that wasn't added before.
        """
        for client in clients:
            if client not in self.__map_client_servers:
                self.place_client(client, server)
            self.__map_client_servers[client][server] = multiplicative_factor
            self.__map_server_clients[server][client] = multiplicative_factor

