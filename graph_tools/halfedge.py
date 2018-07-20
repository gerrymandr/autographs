
import geopandas as gpd
import pysal as ps
import numpy as np
from collections import deque


class Vertex:
    def __init__(self, label, point, data=None):
        """
        Initializes a vertex object.
        :label:     Label (i.e. name) for this vertex.
        :point:     Position of the vertex in an embedding.
        :data:      Data associated with this vertex.
        :returns:   None
        """

        """
        Properties.
        :label: Label of the vertex.
        :point:     Where this vertex has been mapped to in an embedding.
        :data:      Any data associated with this vertex.
        :edges:     Set of outgoing edges from this vertex.
        """
        self.label = label
        self.point = point
        self.data = data

        self.edges = deque()

    def addEdge(self, edge):
        """
        Add an outgoing edge to this vertex.
        :edge:      Edge object with this vertex as the tail.
        :returns:   None
        """
        self.edges.append(edge)

    @property
    def x(self):
        """
        Get the x-coordinate in (an assumed) 2d embedding.
        :returns: Number; x-coordinate.
        """
        return self.point[0]

    @property
    def y(self):
        """
        Get the y-coordinate in (an assumed) 2d embedding.
        :returns: Number; y-coordinate.
        """
        return self.point[1]

    @property
    def xy(self):
        """
        Get the (x,y) coordinate pair in (an assumed) 2d embedding.
        :returns: Tuple; (x,y) coordinate pair.
        """
        return self.x, self.y

    def __eq__(self, other):
        """
        Checks equality between two Vertex objects.
        :other:     Vertex to be compared to.
        :returns:   Boolean; are `self` and `other` the same?
        """
        return self.label == other.label or self.point == other.point

    def __hash__(self):
        """
        Implements a hashing method so that we can quickly look up vertices
        without sacrificing performance.
        :returns: None
        """
        return hash((self.label, self.point))


class Edge:
    def __init__(self, tail, head):
        """
        Initializes an edge object.
        :tail:      Vertex the edge is coming from.
        :head:      Vertex the edge is going to.
        :returns:   None
        """

        """
        Properties.
        :tail:      Starting vertex of this edge.
        :head:      Ending vertex of this edge.
        :traversed: Has this edge been traversed yet?
        """
        self.tail = tail
        self.head = head
        self.traversed = False

    def __eq__(self, other):
        """
        Checks equality between two Edge objects.
        :other:     Edge object to be compared to.
        :returns:   Boolean; are `self` and `other` the same?
        """
        return self.tail == other.tail and self.head == other.head


class HalfEdge:
    def __init__(self, path):
        """
        Initializes a half-edge structure for the given file.
        :path:      Path to a data file.
        :returns:   None
        """

        """
        Properties.
        :_adjacency:    Adjacency matrix with each vertex's neighbors ordered
                        (by angle with respect to the ray (0,1)).
        """
        self.adjacency = {}

        # Get the file and create vertices (and their adjacencies).
        df = gpd.read_file(path)
        contiguity = ps.weights.Contiguity.Rook.from_dataframe(df)
        centroids = df.centroid

        # Initialize vertices.
        for label, _ in enumerate(contiguity):
            x, y = centroids[label].xy
            v = Vertex(label, (x[0], y[0]))
            self.adjacency[v] = None

        # Go over the adjacency matrix, adding half-edges. Create an external
        # list of unordered neighbors, then order them.
        for index, vertex in enumerate(self.adjacency.keys()):
            unordered = []

            # Since we don't have the neighbors properly set up, we have to
            # iterate over them in a weird way. However, it ends up alright.
            for uncoded_neighbor in contiguity[index].keys():
                # Get the correct neighbor.
                neighbor = list(self.adjacency.keys())[uncoded_neighbor]

                # Create a new Edge object and mark that it hasn't been traversed.
                e = Edge(vertex, neighbor)
                vertex.addEdge(e)
                
                # Find the angle between `vertex` and `neighbor`. Basically just
                # took this code from Eugene.
                xdelta = vertex.x - neighbor.x
                ydelta = vertex.y - neighbor.y
                angle = np.arctan2(xdelta, ydelta)
                unordered.append((neighbor, angle))

            # Order the collection of vertices by neighbor, freeze the order in a
            # tuple, then stick it in the adjacency matrix.
            ordered = sorted(unordered, key=lambda n: n[1])
            self.adjacency[vertex] = tuple([tup[0] for tup in ordered])
   

if __name__ == "__main__":
    he = HalfEdge("../test/data/tl_2016_19_cousub/tl_2016_19_cousub.shp")