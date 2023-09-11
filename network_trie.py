"""
FIT2004 Assignment2
Name: Shosuke Asano
Student ID: 32201303
"""

"""
Part 1
""" 

class ResidualNetwork:
    """
    The ResidualNetwork class converts the problem of fast backups into a residual network with connections and data centers. 
    The connections are represented as edges in the graph concept, and the data centers are represented as vertices in the graph concept. 
    Additionally, this residual network is represented using an adjacency list.

	Input:
        connections: A list representing the direct communication channels between the data centres (data centre, data centre, the maximum throughput of that channel)
        maxIn: A list representing the maximum amount of incoming data per second for each data centre
        maxOut: A list representing the maximum amount of outgoing data per second for each data centre
        targets: A list representing the data centres that are deemed appropriate locations for the backup data to be stored.

    Time complexity: O(D+C), where D is the number of data centres, and C is the number of communication channels.
    Auxiliary space complexity: O(D+C), where D is the number of data centres, and C is the number of communication channels.
    """
    def __init__(self, connections, maxIn, maxOut, target):
        """
        Function description: Constructor for Residual Network. It creates Connection objects and Data Centre objects. 
        Each data centre is divided into 3 vertices and a super target to represent the maximum amount of incoming data and outgoing data with connections (edges). 
        The super target gathers multiple targets into a single target.
        
        Input:
            connections: A list representing the direct communication channels between the data centres (data centre, data centre, the maximum throughput of that channel)
            maxIn: A list representing the maximum amount of incoming data per second for each data centre
            maxOut: A list representing the maximum amount of outgoing data per second for each data centre
            targets: A list representing the data centres that are deemed appropriate locations for the backup data to be stored.

		Time complexity: O(C), where C is the number of communication channels.
        Auxiliary space complexity: O(C), where C is the number of communication channels.
        """
        # creating a list to save the Connection objects based on the number of data centres
        self.dc = [None] * (self.getNumOfDC(maxIn) + 1)
        # the number of data centres in residual network (number of data centre based on input + data centre for super target)
        self.length = self.getNumOfDC(maxIn) + 1

        # creating Connection objects and save it into dc list 
        for id in range(self.length):
            self.dc[id] = Connection(id)            

        # creating data centre objects for each connection
        self.createDC(self.createConnections(connections, maxIn, maxOut))

        # creating data centre objects for the connections of the super target
        self.superTarget(target, maxIn)

    def getNumOfDC(self, dc_list):
        """
        Function description: It returns the number of data centres of residual network. Since each data centre is broken down into 3 vertices to 
        describe the max incoming and outgoing data, the number of data centres will be 3 times of the numbner of current data centres.
        
        Input: 
            dc_list: A list containig the max incoming or outgoing data
        Output: the number of data centres to build residual network
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        """
        return 3 * len(dc_list)
    
    def createDC(self, connections):
        """
        Function description: This function creates DataCentre objects for each connection except for super target.

        Input: 
            connections: A list representing the direct communication channels between the data centres (data centre, data centre, the maximum throughput of that channel)
        Output: 
            There is no output. DataCentre objects that for each connection will be created. 
        Time complexity: O(C), where C is the number of communication channels.
        Auxiliary space complexity: O(C), where C is the number of communication channels.
        """
        for edge in connections:
            # creating DataCentre object in adjancy list of the connection. 
            self.dc[edge[0]].edges.append(DataCentre(edge[0],edge[1],edge[2]))

    def createConnections(self, connections, maxIn, maxOut):
        """
        Function description: Based on connections input, it returns new connection list. Each data centre expanded three data centres for 
        the maximum amout of incoimg data and the maximum amount of outgoing data, and the new conncetions of the new data centres are created.

        Input: 
            connections: A list representing the direct communication channels between the data centres (data centre, data centre, the maximum throughput of that channel)
        Output: 
            A list representing the updated direct communication channels between the data centres (data centre, data centre, the maximum throughput of that channel)
        Time complexity: O(C), where C is the number of communication channels. 
        Auxiliary space complexity: O(C), where C is the number of communication channels.
        """
        new_connections = []
        # connection for the maximum throughput of the channel
        for i in range(len(connections)):
            new_connections.append((2*connections[i][0] + len(maxIn) + 1, 2*connections[i][1] + len(maxIn), connections[i][2]))

        for id in range(len(maxIn)):
            new_connections.append((2*id + len(maxIn), id, maxIn[id]))            # connection for the maximum amount of incoimg data
            new_connections.append((id, 2*id + len(maxIn) + 1, maxOut[id]))       # connection for the maximum amount of outgoing data

        return new_connections
    
    def superTarget(self, targets, maxIn):
        """
        Function description: This function creates DataCentre objects for a connection of the super target (multiple targets are combined).

        Input: 
            targets: A list representing the data centres that are deemed appropriate locations for the backup data to be stored.
            maxIn: A list representing the maximum amount of incoming data per second for each data centre
        Output: 
            There is no output. DataCentre objects for super target (gathering multiple targets into only one target) will be created. 
        Time complexity: O(T), where T is the number of targets.
        Auxiliary space complexity: O(1)
        """
        for dataCentre in targets:
            # creating DataCentre object in adjancy list of the connection.
            self.dc[dataCentre].edges.append(DataCentre(dataCentre, self.length - 1, maxIn[dataCentre]))

        

    def minFlow(self, path):
        """
        Function description: This function returns the minimum flow of the input augmenting path. 

        Input: 
            path: A list representing an augmenting path from the source to the target.
        Output:
            An integer representing the minimum flow of the augmenting path.
        Time complexity: O(C), where C is the number of connections.
        Auxiliary space complexity: O(1)
        """
        min = float('inf')
        for dataCentre in range(len(path)-1):
            for e in self.dc[path[dataCentre]].edges:
                # if a connection between the data centres exists
                if (e.v == path[dataCentre+1] and e.capacity < min):
                    min = e.capacity
        return min        

    def update_residual_network(self, path, flow):
        """
        Function description: This function updates the residual network based on the input path and minimum flow. 
        Based on the minimum flow, the capacity of a connection decreases, and the capacity of the reverse connection increases. 
        If the connection does not exist, it creates new connection. In addition, it remove the connection if the capacity of the connection is 0.

        Input:
            path: A list representing an augmenting path from the source to the target.
            flow: An integer representing the minimum flow of the path. 
        Output:
            There is no output. The residual network will be updated 
        Time complexity: O(C), where C is the number of connections.
        Auxiliary space complexity: O(1)
        """
        # the capacity of a connection decreases
        for dataCentre in range(len(path)-1):
            for e in self.dc[path[dataCentre]].edges:
                # if a connection between the data centres exists
                if (e.v == path[dataCentre+1]):
                    e.capacity -= flow
                    # whent the capacity is 0, remove the connection
                    if (e.capacity == 0):
                        self.dc[path[dataCentre]].edges.remove(e)

        # the capacity of the reverse connection increases
        path.reverse()         
        for dataCentre in range(len(path)-1):
            has_connection = False
            for e in self.dc[path[dataCentre]].edges:
                # if a connection between the data centres exists
                if (e.v == path[dataCentre+1]):
                    has_connection = True
                    e.capacity += flow
            # if there is no connection, crete new connection
            if has_connection == False:
                self.dc[path[dataCentre]].edges.append(DataCentre(path[dataCentre], path[dataCentre+1], flow))

    def ford_fulkerson(self, source, maxIn):
        """
        Function description: This function represents Ford-Fulkerson method. It finds the maximum throughput from the soure to the target. 
        It keeps finding a augmenting path and updates the residual network based on the augmenting path until it cannot find 
        an augmenting path from the source to the target. 

        Input:
            source: An integer representing a source data centre
           
        Output:
            An integer representing a maximum throughput from the source to the target
        Time complexity: O(DC^2), where D is the number of data centres, and C is the number of communication channels.
        Auxiliary space complexity: O(D), where D is the number of data centres. 
        """
        max_flow = 0
        while self.augmenting_path(source, maxIn) != []:
            augmenting_path = self.augmenting_path(source, maxIn)
            min_flow = self.minFlow(augmenting_path)
            max_flow += min_flow
            self.update_residual_network(augmenting_path, min_flow)
        return max_flow
    

    def augmenting_path(self, source, maxIn):
        """
        Function description: This function finds a path from a source to a target with bfs technique, and returns an augmenting path. 

        Input: 
            source: An integer representing a source data centre
           
        Output:
            A list representing an augmenting path from the source to the target.
        Time complexity: O(D+C), where D is the number of data centres, and C is the number of communication channels.
        Auxiliary space complexity: O(D), where D is the number of data centres. 
        """
        target = self.length - 1            # super target
        possible_route = []
        discovered = []
        discovered.append(self.dc[source])  # put connection object into discovered list
        self.dc[source].discovered = True   # start data centre is discovered
        while len(discovered) > 0:
            dataCentre = discovered.pop(0)         # get connection object
            dataCentre.visited = True 
            possible_route.append(dataCentre.id)
            if self.dc[target].visited == True:
                break 
            for i in range(len(dataCentre.edges)):    # loop the list that the connection can move
                adj = dataCentre.edges[i].v           # get the neighbors of the connection
                if self.dc[adj].discovered == False: 
                    discovered.append(self.dc[adj])   # put connection object into discovered list
                    self.dc[adj].discovered = True    # the data centre is discovered  
                    self.dc[adj].previous = dataCentre

        # if no path from source to target
        if target not in possible_route:
            return []

        # trace back and get the shortest path
        path = []
        location = target
        path.append(target)      
        while source != location:
            route = self.dc[location].previous.id    # get the previous vertex of the current vertex
            path.append(route)
            location = self.dc[route].id             # update the current vertex 
        path.reverse()

        # set the attributes of connection objects to the default value for multipe times searching of an augmenting path in the future
        for obj in self.dc:
            obj.discovered = False        
            obj.visited = False           
            obj.previous = None
            
        return path
    

class Connection:
    """
    Connection class contains the information of each connection.
        id: An integer representing the id of connection
        edges: the connected data centres of the current data centre
        discovered: boolean representing if the data centre is discovered or not 
        visited: boolean representing if the data centre is visited or not 
        previous: the previous data centre that was visited 
    Input:
        id: An integer representing the id of connection
    Time complexity: O(1)
    Auxiliary space complexity: O(1)
    """
    def __init__(self, id):
        """
        Function description: Constructor for Connection. The attributes are initilized. The connection of id is taken to distiguish each connection.

        Input:
            id: An integer representing the id of connection
		Time complexity: O(1)
        Auxiliary space complexity: O(1)
        """
        self.id = id                   # id of the connection
        self.edges = []                # possible path from the data centre
        self.discovered = False        
        self.visited = False           
        self.previous = None           # previous data centre of the current data centre


class DataCentre:
    """
    DataCentre class contains the information of the connection. Date centre u connects data centre v. 
    In addition, the capacity represents the capacity of the connection u - v

    Input: 
        u: data centre (starting data centre of the connection)
        v: data centre (ending data centre of the conection)
        capacity: the capacity that the channel can go through
    Time complexity: O(1)
    Auxiliary space complexity: O(1)
    """
    def __init__(self, u, v, capacity):
        """
        Function description: Constructor for DataCentre. It initializes the information of the connection from data centre u to data centre v. 
            u: data centre (starting data centre of the connection)
            v: data centre (ending data centre of the conection)
            capacity: the capacity that the channel can go through
		Time complexity: O(1)
        Space complexity: O(1)
        """
        self.u = u                     # starting data centre of the connection
        self.v = v                     # ending data centre of the conection
        self.capacity = capacity       # the capacity of the channel


def maxThroughput(connections, maxIn, maxOut, origin, targets):
    """
        Function description: 
            This function computes the maximum throughput from the source to the targets with Ford-Fulkerson method. 

        Approach description:
            I convert Fast Backups problem into residual network and compute the maximum throughput from the source to the targets with Ford-Fulkerson method.
            I created residual network based on the input. In order to represent the maximum amount of incoming data and the maximum amount of outgoing data of each data centre, 
            I added two more data centres for each data centre. One data centre connects to the original data centre to represent the maximum amount of incoming data, 
            and the original data centre connects to another data centre to represent the maximum amount of outgoing data. 
            In addition, it can be easy to apply Ford-Fulkerson method by combining multiple targets into one super target based on the maximum amount of incoming data to the targets. 
            Lastly, it finds the maximum throuputs from the source to the target by keep finding an augmenting path and updating the residual network. 
            
            For time complexity, since ford_fulkersomethod is implemented, O(DC^2).
            For space complexity, since residual network is created, O(C).
    
		Input: 
            connections: A list representing the direct communication channels between the data centres (data centre, data centre, the maximum throughput of that channel)
            maxIn: A list representing the maximum amount of incoming data per second for each data centre
            maxOut: A list representing the maximum amount of outgoing data per second for each data centre
            origin:  An integer representing a source data centre
            targets: A list representing the data centres that are deemed appropriate locations for the backup data to be stored.

        Output: 
            An integer representing a maximum throughput from the source to the target

		Time complexity: O(DC^2), where D is the number of data centres, and C is the number of communication channels.
        Auxiliary space complexity: O(C), where C is the number of communication channels.     
    """
    residual_network = ResidualNetwork(connections, maxIn, maxOut, targets)
    return residual_network.ford_fulkerson(origin, maxIn)




"""
Part 2
""" 
class CatsTrie:
    """
    CatsTrie class represents a Trie data structure. It uses Node objects and creates data strucure for multiple words. 

	Input:
        sentences: A list of string that encapsulates all of the cat sentences.

    Time complexity: O(NM), where N is the number of sentence in sentences, and M is the number of characters in the longest sentence.
    Space complexity: O(NM), where N is the number of sentence in sentences, and M is the number of characters in the longest sentence.
    """
    def __init__(self, sentences):
        """
        Function description: Constructor for CatsTrie. By inserting each word of the input sentences, the Trie data structure is created. 
        
        Input:
            sentences: A list of string that encapsulates all of the cat sentences.

		Time complexity: O(NM), where N is the number of sentence in sentences, and M is the number of characters in the longest sentence.
        Space complexity: O(NM), where N is the number of sentence in sentences, and M is the number of characters in the longest sentence.
        """
        self.root = Node()             # root node
        self.sentences = sentences

        # create Trie data structure for the words 
        for word in sentences:
            self.insert(word)
        
        # update leaf_node
        for word in sentences:
            self.update_node(word)
    
    def insert(self, word):
        """
        Function description: This function insert the input word in Trie data structure. 
        The frequency of each character and the previous node of the current node are updated.
        
        Input:
            sentences: A list of string that encapsulates all of the cat sentences.
        Output:
            There is no output. A word is inserted in Trie
		Time complexity: O(M), M is the number of characters in the longest sentence.
        Space complexity: O(M), M is the number of characters in the longest sentence.
        """
        current = self.root        # start from root

        # insert each character in Trie
        for chr in word:
            index = ord(chr) - 97 + 1            # convert chracter into ASCII code
            pervious = current                  

            # if path does not exist
            if current.link[index] is None:
                current.link[index] = Node()     # create new path for the index
            current.link[index].frequency += 1 
            current = current.link[index]        # move next Node
            current.previous = pervious
        
        # insert a terminal 
        index = 0               # the index of a terminal
        obj = current
        # if path does not exist
        if current.link[index] is None:
            current.link[index] = Node()     # create new path for the index
        current.link[index].frequency += 1
        current = current.link[index]        # move next Node
        current.previous = obj
        current.word = word                  # save output word in the leaf node

        # update the most frequent word of Trie
        if (self.root.leaf_node == None) or (current.frequency > self.root.leaf_node.frequency) or (current.frequency == self.root.leaf_node.frequency and self.root.leaf_node.word > word):
            self.root.leaf_node = current

    def update_node(self, word):
        """
        Function description: This function updates the leaf_node information of each node based on the frequency and lexical order.
        The leaf_node represents the implicit connection between the current node and the leaf node that contains a word.
        
        Input:
            sentences: A list of string that encapsulates all of the cat sentences.
        Output:
            There is no output. The leaf_node will be updated. 
		Time complexity: O(M), M is the number of characters in the longest sentence.
        Space complexity: O(1)
        """
        current = self.root
        
        # get the leaf node
        for chr in word:
            index = ord(chr) - 97 + 1       # convert chracter into ASCII code
            current = current.link[index]

        index = 0       # the index of a terminal
        leaf = current.link[index]          # leaf node of each word
        
        # traverse from the leaf to the root
        while current.previous != None:     # unless the previous node of the current is root
            # if current node does not connect to a leaf
            if current.leaf_node == None:
                current.leaf_node = leaf
            # if current node connects to a leaf node
            else:
                # compare the frequency
                if (current.leaf_node.frequency < leaf.frequency): 
                    current.leaf_node = leaf
                # if the frequency is same, compare the lexical order
                elif (current.leaf_node.frequency == leaf.frequency) and (current.leaf_node.word > leaf.word): 
                    current.leaf_node = leaf
            current = current.previous
    

    def autoComplete(self, prompt):
        """
        Function description: 
            This function returns a complete word based on the prompt. This function has similar behaviour of auto-completed system of key-board.
            If the prompt exists in the Trie data structure, it will return the most frequent word, otherwise return None.
            If the freqency is same, it will return a word that is lexicographically small.

        Approach description:
            In the process of inserting all words into the Trie, I save the complete word in the leaf node (this is used to return a complete word). 
            Additionally, I saved the frequency of characters into each node. 
            The frequency of the character occurence that is saved in each node helps the decision of choosing the complete sentence. 
            Other node does not save complete word to reutrn. However, each node has implicit connection to the leaf node that returns the complete word based on the highest frequency. 
            The root node has implicit connection to the leaf node that has the most frequent word in the Trie.
            
            For time complexity, it traverse the prompt. Thus, O(X).
            For space complexity, since no additional space used. Thus, O(1).

		Input: 
            prompt: A String (a - z) representing incomplete sentence that is to be completed by the trie.

        Output: 
            A String representing the completed sentence from the prompt. If such a word doe not exist, return None

		Time complexity: O(X), where X is the length of the prompt. 
		Aux space complexity: O(1)
        """
        if prompt == "":
            return self.root.leaf_node.word
        else:
            current = self.root
            # traverse the prompt
            for chr in prompt:
                index = ord(chr) - 97 + 1           # convert chracter into ASCII code
                # if path does not exist
                if current.link[index] is None:
                    return None
                # if path exists
                else:
                    current = current.link[index]
            return current.leaf_node.word



class Node:
    """
    Node class contains the information of the node. Node plays a role to store data, and only a - z and $ (terminal) character can be stored in the data structure. 
        word: A string representing an output word
        link: A list representing the storage to save node objects. The index represents the alphbet ($, a - z)
        frequency: An integer representing the frequency of the character
        leaf_node: A leaf node object can be stored
        previous: the previous node of the current node
    
    Time complexity: O(1)
    Auxiliary space complexity: O(1)
    """
    def __init__(self):
        """
        Function description: Constructor for Node. It initializes the attributes of the node. This helps to track the most frequent word. 
        In link, the new node will be saved, and the index 0 of the link represents the terminal $ and the index 1 - 26 represents the character a - z. 

            word: A string representing an output word
            link: A list representing the storage to save node objects. The index represents the alphbet ($, a - z)
            frequency: An integer representing the frequency of the character
            leaf_node: A leaf node object can be stored
            previous: the previous node of the current node

		Time complexity: O(1)
        Space complexity: O(1)
        """
        self.word = None            
        self.link = [None] * 27      # character a to z and $ (for terminal)
        self.frequency = 0           # frequency of the character
        self.leaf_node = None
        self.previous = None         # the previous node

