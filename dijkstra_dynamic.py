"""
FIT2004 Assignment1
Name: Shosuke Asano
Student ID: 32201303
"""

"""
Part 1
""" 

"""
    <<CITATION>>
    Title: FIT2004 course notes
    Author: FIT2004 teaching team, Daniel Anderson
    
    Title: FIT1008 week12 Slides for the lesson on "Heap 1" and Slides for the lesson on "Heap 2"
    Author: Prepared by Maria Garcia de la Banda, Updated by Brendon Taylor
    
    Title: FIT1008 week12 Slides for the lesson on "Heap 2"
    Author: Prepared by Maria Garcia de la Banda, Updated by Brendon Taylor
"""
class MinHeap():
    """
    Heap such that the root node has minimum value in the array.
    Space Complexity: O(n),where n is the number of items in the MinHeap
    """
    def __init__(self):
        """
        Function description: Constructor for MinHeap
		Time complexity: O(1)
        Space Complexity: O(1)
        """
        self.array = [None]
        self.length = 0 
    
    def insert(self, data, key):
        """
        Function description: Add a data and a key to MinHeap's array
        Time Complexity: O(log n), where n is the number of items in the MinHeap
        Space Complexity: O(1)
        Input: 
            data: Any data type that is saved in data
            key: An integer representing
        """
        self.array.append((data, key))
        self.length += 1 
        self.rise(self.length)
    
    def serve(self):
        """
        Function description: The item that has smallest key is removed and returned as output. 
        Time Complexity: O(log n), where n is the number of items in the MinHeap.
        Space Complexity: O(1)
        Output: Any data type that is saved in data 
        """
        self.swap(1, self.length)
        self.length -= 1 
        self.sink(1)
        return self.array.pop()[0]  # return data
    
    def update(self, data, key):
        """
        Function description: Update the corresponding data's key to new key
        Time Complexity: O(log n), where n is the number of items in the MinHeap
        Space Complexity: O(1)
        Input: 
            data: Any data type that is saved in data
            key: An integer representing
        Output: New key is replaced to old key
        """
        for i in range(1, self.length+1):
            if self.array[i][0] == data:
                old_key = self.array[i][1]
                self.array[i] = (data, key)  
                if key < old_key:             # comparing with its parent node
                    self.rise(i)    
                else:                         # comparing with its child node
                    self.sink(i)

    def swap(self, x, y):
        """
        Function description: Swap two number's position in the array
        Time Complexity: O(1)
        Space Complexity: O(1)
        Input:
            x: An integer representing a index
            y: An integer representing a index
        """
        self.array[x], self.array[y] = self.array[y], self.array[x]
    
    def rise(self, element):
        """
        Function description: Adjusts the position of the element by comparing with its parent nodes
        Time Complexity: O(log n), where n is the number of items in the MinHeap
        Space Complexity: O(1)
        Input: An integer 
        """
        parent = element // 2 
        while parent >= 1:
            if self.array[parent][1] > self.array[element][1]:  # comparing with its parent node
                self.swap(parent, element)
                element = parent 
                parent = element // 2
            else:
                break           # correct position
    
    def sink(self, element):
        """
        Function description: Adjusts the position of the element accordingly by comparing with its child nodes 
        Time Complexity: O(log n), where n is the number of items in the MinHeap
        Space Complexity: O(1)
        Input: An integer 
        """
        child = 2*element 
        while child <= self.length: 
            if child < self.length and self.array[child+1][1] < self.array[child][1]:  # comparing with its child node
                child += 1 
            if self.array[element][1] > self.array[child][1]:
                self.swap(element, child)
                element = child 
                child = 2*element 
            else:
                break           # correct position


class Graph:
    """
    Graph class makes roads to graph, and manages the key location of the graph and connected roads with adjacency list. 
	Input: 
         passengers: A list representing the location of passengers
         G: A list that contains a graph information (vertex, vertex, driving minutes if alone, driving minutes if there is passengers)
    """
    def __init__(self, passengers, G):
        """
        Function description: Constructor for Graph. It creates Vretex object and Edge object for each vertex.  
        Input: A list that contains a graph information (vertex, vertex, driving minutes if alone, driving minutes if there is passengers)
		Time complexity: O(R+L+P), where R is the number of edge (roads), L is the number of vertices (key location) and P is the number of passengers. 
        Auxiliary space complexity: O(R+L), where R is the number of edge (roads) and L is the number of vertices (key location). 
        """
        # creating a list to save the Vertex objects based on the number of vertices in Graph
        self.vertices = [None] * self.getNumOfVerticies(G)
        
        # creating Vertex object and save it into vertices list
        for i in range(self.getNumOfVerticies(G)):
            self.vertices[i] = Vertex(i)

        # creating Edge objects for each vertex
        self.addEdgeAndWeight(G)
        
        # when there is passenger at the vertex, change the passenger status to True
        for passenger in passengers:
            self.vertices[passenger].passengers = True

    def getNumOfVerticies(self, v):
        """
        Function description: This function returns the number of vertices.
        Input: A list that contains a graph information (vertex, vertex, driving minutes if alone, driving minutes if there is passengers)
        Output: An integer representing the number of vertices 
		Time complexity: O(L), where L is the number of vertex (key locations)
        Auxiliary space complexity: O(1)
        """    
        ret = 0
        for m in range(len(v)):
            currernt = max(v[m][0], v[m][1])
            if currernt > ret:
                ret = currernt
        return ret+1
    
    def addEdgeAndWeight(self, edg):
        """
        Function description: This function creates Edge objects for each vertex.
        Input: A list that contains a graph information (vertex, vertex, driving minutes if alone, driving minutes if there is passengers)
		Time complexity: (R), where R is the number of edge (roads).
        Auxiliary space complexity: O(R), where R is the number of edge (roads).
        """  
        for edge in edg:
            # creating Edge object in adjancy list of the vertex. 
            self.vertices[edge[0]].edges.append(Edge(edge[0],edge[1],edge[2],edge[3]))

    def dijkstra(self, start, reverse):
        """
        Function description: 
            This function implements dijkstra algorithm. 
            This function finds the shortest distance from start location to end location when you are driving alone.
            
        Input:
            start: An integer representing the start location
            reverse: A boolean type. If I wanna get reverse graph, True, otherwise False. 
        Output:
            There is no output. However, distance and previous vertex information are saved in each vertex object. 
        Time complexity: O(RlogL), where R is the number of edge (roads) and L is the number of vertices (key location). 
        Auxiliary space complexity: O(L+R), where R is the number of edge (roads) and L is the number of vertices (key location). 
        """
        vx = self.vertices[start]    # get Vertex object of the start location
        vx.distance = 0              # set the start vertex distance is 0
        discovered = MinHeap()   
        discovered.insert(vx, 0)         # put Vertex object into discovered list and the key is distance 
        vx.discovered = True             # start vertex is discovered
        while discovered.length > 0:     
            item = discovered.serve()    # get Vertex object that has minimum distance from the heap
            item.visited = True          # The distance of the vertex is finalized
            for edge in item.edges:       
                adj = edge.v             # get the connected vertex number of the item
                if self.vertices[adj].discovered == False:                  
                    self.vertices[adj].discovered = True 
                    if reverse == True:  
                        self.vertices[adj].distance = item.distance + edge.x
                    else:
                        self.vertices[adj].distance = item.distance + edge.w                 # distance from the start location is saved
                    self.vertices[adj].previous = item                                       # previous vertex is saved 
                    discovered.insert(self.vertices[adj], self.vertices[adj].distance)       # put Vertex object into discovered list
                elif self.vertices[adj].visited == False:
                    # when there are passengers
                    if reverse == True:                                       
                        if self.vertices[adj].distance > item.distance + edge.x:                 # if finding new shortest route
                            self.vertices[adj].distance = item.distance + edge.x                 # distance from the start location is saved
                            self.vertices[adj].previous = item                                   # previous vertex is saved 
                            discovered.update(self.vertices[adj], self.vertices[adj].distance)   # update the distance of corresponding vertex in heap
                    # when driving alone
                    else:                 
                        if self.vertices[adj].distance > item.distance + edge.w:                 # if finding new shortest route
                            self.vertices[adj].distance = item.distance + edge.w                 # distance from the start location is saved
                            self.vertices[adj].previous = item                                   # previous vertex is saved 
                            discovered.update(self.vertices[adj], self.vertices[adj].distance)   # update the distance of corresponding vertex in heap

    def shortest_route(self, start, end):
        """
        Function description: This function traces back the previous vertex and returns a shortest route from start to end.
        Input: 
            start: An integer representing the start location 
            end: An integer representing the end location 
        Output: A list representing the route from start location to end location
		Time complexity: O(L), where L is the number of key locations
        Auxiliary space complexity: O(L), where L is the number of key locations
        """   
        # trace back and get the shortest path
        shortest_route = []
        location = end
        shortest_route.append(location)      
        while start != location:
            route = self.vertices[location].previous.vertex    # get the previous vertex of the current vertex
            shortest_route.append(route)
            location = self.vertices[route].vertex             # update the current vertex 
        shortest_route.reverse()
        return shortest_route


class Vertex:
    """
    Vertex class represents key locations in roads, and manages the information of each vertex. The information is 
        vertex: the number of vertex
        edges: the connected vertices of a vertex
        discovered: boolean representing if the vertex is discovered or not 
        visited: boolean representing if the vertex is visited or not 
        distance: distance from a vertex
        previous: the previous vertex that was visited 
	Input: An integer representing the vertex number
    Time complexity: O(1)
    Auxiliary space complexity: O(1)
    """
    def __init__(self, vertex):
        """
        Function description: Constructor for Vertex class. Initialize necessary elements.
        Input: An integer representing the vertex number
		Time complexity: O(1)
        Auxiliary space complexity: O(1)
        """  
        self.vertex = vertex           # id of the vertex
        self.edges = []                # possible path from the vertex
        self.discovered = False        
        self.visited = False           
        self.distance = float('inf')   
        self.previous = None           # previous vertex of the vertex
        self.passengers = False        # whether there is a passenger or not at the vertex(location)


class Edge:
    """
    Edge class represents pah from a key location to another key location, and manages driving time (the weight of the edge). 
    Time complexity: O(1)
    Auxiliary space complexity: O(1)
    """
    def __init__(self, u, v, w, x):
        """
        Function description: Constructor for Edge. 
        Input: 
            u: vertex (starting location of the road)
            v: vertex (ending location of the road)
            w: driving time from u to v if you are alone in the car
            x: driving time from u to v if there are 2 or more persons in the car.
		Time complexity: O(1)
        Space complexity: O(1)
        """  
        self.u = u
        self.v = v
        self.w = w
        self.x = x


def optimalRoute(start, end, passengers, roads):
    """
        Function description: 
            This function computes the optimal route of roads based on the driving time, 
            and return a route such that it takes the minimum driving time in all possible way. 

        Approach description:
            By creating two graphs (normal graph and reverse graph), I compute the driving time from start to each passenger locations  
            with normal graph and the driving time from end to each passenger locations with reverse graph since dijkstra compute the minimum driving time 
            from a source. After that, I can get the minimum driving time with the total driving time from start location to end location when you pick up a passenger.
            Since you can choose not to pick up the passenger if driving time is shorter. 
            I lastly compare the driving times when you pick up a passenger and do not pick up a passenger. 
            The smaller driving time is choosen as the optimal route.
            
            For time complexity, dijkstra function is implemented twice, and otehr time complexity is smaller than RlogL. Thus, O(RlogL).
            For space complexity, since dijkstra function is implemented twice, O(L+R).
    
		Input: 
            start: An integer representing the starting location of the optimal route.
            end: An integer representing the ending location of the optimal route.
            passengers: A list representing the locations of the passengers.
            roads: A list representing each edge information that contains (location, location, driving time if alone, driving time if there are passengers)

        Output: 
            A list that contains the path for optimal route.

		Time complexity: 
            O(RlogL), where R is the number of edge (roads) and L is the number of vertices (key location).

		Aux space complexity: 
            O(L+R), where R is the number of edge (roads) and L is the number of vertices (key location). 

    """
    graph = Graph(passengers, roads)          # creating new Graph object
    graph.dijkstra(start, False)              # implement dijkstra from the start location
    
    # reverse the edge of the graph
    for i in range(len(roads)):
        a,b,c,d = roads[i][0],roads[i][1],roads[i][2],roads[i][3]
        roads[i] = (b,a,c,d)
    
    reverse_graph = Graph(passengers, roads)   # creating new Graph object (the edges are reversed)
    reverse_graph.dijkstra(end, True)          # implement dijkstra from the end location
    

    if passengers == []:                       # when there is no passenger location    
        route = graph.shortest_route(start, end)
    # compute the best passenger pick up location
    else:                                     
        minimum_distance = float('inf')     
        for vertex in passengers:
            distance = graph.vertices[vertex].distance + reverse_graph.vertices[vertex].distance    # total distance from start to end
            if distance < minimum_distance:
                minimum_distance = distance             
                minimum_distance_vertex = vertex         # vertex of passenger that has minimum distance 
        # comparing with the distance when ther are passengers and the distance when you are driving alone
        if graph.vertices[end].distance < minimum_distance:
            route = graph.shortest_route(start, end)
        else:
            lst = reverse_graph.shortest_route(end, minimum_distance_vertex)        # shortest path from end to the vertex
            lst.pop()         # remove the last vertex since it's duplicate
            lst.reverse()
            route = graph.shortest_route(start, minimum_distance_vertex) + lst      # concatinate the list and make it from start to end
    return route








"""
Part 2
""" 
def select_sections(occupancy_probability):
    """
        Function description: 
            This function returns an output list containing the sum of occupancy that is minimum in all possible ways, 
            and the locations in each row to get the minimum total occupancy.

        Approach description:
            In each row of occupancy_probability, I calculate the total occupancy rate at the each position
            by comparing the above adjacency itme and get the minimum item in the above adjacency itme. 
            I save the minimum total occupancy that the item can take into a new list of lists. 
            By doing so, I can see the smallest total occupancy in each row. 
            In order to get each location of the minimum total occupancy that goes through, 
            it loop through each row and get the location that has minimum total occupancy in the row.
            time complexity: O(NM) because it loop through each item of (n × m) list of lists. 
            In addition, backtrack part is also O(N). Thus, the time complexity is O(NM).
            space complexity: O(NM) because new (n × m) list of lists is created to save the total occupancy in each position.
        
		Input: 
            occupancy_probability: a list of lists containing integers (0 from 100)

        Output: 
            A list that contains two items. First item (minimum total occupancy) is the total occupancy for the selected n sections to be removed.
            Second item is the routes to get the minimum total occupancy. Each location is represented with a tuple.

		Time complexity: 
            O(NM), where N is the number of rows and M is the number of columns

		Aux space complexity: 
            O(NM), where N is the number of rows and M is the number of columns
		
	"""
    n = len(occupancy_probability)     # num of rows
    m = len(occupancy_probability[0])  # num of columns
    
    # creating (n × m) list of lists having 0 in all elements except for first row
    memo = [[-1 for _ in range(m)] for _ in range(n)]
    memo[0] = occupancy_probability[0] 

    # adding value into memo matrix
    for i in range(1, n):
        for j in range(m):
            x = memo[i-1][j]                   # the item above in previous row
            if j != 0:     # when j == 0, there is no item at memo[i-1][j-1]
                x = min(x, memo[i-1][j-1])     # comparing the above item and left above item in previous row
            if j != m-1:   # when j == m-1, there is no item at memo[i-1][j+1]
                x = min(x, memo[i-1][j+1])     # comparing the minimum item (above item or left above item) and right above item in previous row
            # memo[i][j] = minimum adjacency item of occupancy_probability[i][j] + occupancy_probability[i][j]
            memo[i][j] = x + occupancy_probability[i][j]          

    # trace back and find a section location in each row
    sections_location = []
    min_in_row = min(memo[n-1])                            # minimum value in the last row 
    minimum_value_index = memo[n-1].index(min_in_row)      # the index of minimum value
    sections_location.append((n-1, minimum_value_index))   
    for i in range(n-2, -1, -1):
        x = memo[i][minimum_value_index]                   # the item above in previous row
        if minimum_value_index != 0:
            x = min(x, memo[i][minimum_value_index-1])     # comparing the above item and left above item in previous row
        if minimum_value_index != m-1:   
            x = min(x, memo[i][minimum_value_index+1])     # comparing the minimum item (above item or left above item) and right above item in previous row
    
        # get the index of the minimum item
        if minimum_value_index == 0:
            if x == memo[i][minimum_value_index]:
                location = minimum_value_index          # minimum value is above item in previous row
            elif x == memo[i][minimum_value_index+1]:
                location = minimum_value_index+1        # minimum value is above right item in previous row
        elif minimum_value_index == m-1:
            if x == memo[i][minimum_value_index]:
                location = minimum_value_index          # minimum value is above item in previous row
            elif x == memo[i][minimum_value_index-1]:
                location = minimum_value_index-1        # minimum value is above left item in previous row
        else:
            if x == memo[i][minimum_value_index]:
                location = minimum_value_index          # minimum value is above item in previous row
            elif x == memo[i][minimum_value_index-1]:
                location = minimum_value_index-1        # minimum value is above left item in previous row
            else:
                location = minimum_value_index+1        # minimum value is above right item in previous row
        sections_location.append((i, location)) 
        minimum_value_index = location

    sections_location.reverse()
    minimum_total_occupancy = min(memo[n-1]) 

    return [minimum_total_occupancy, sections_location]
