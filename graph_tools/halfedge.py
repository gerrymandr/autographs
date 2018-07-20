
class HalfEdge:
    def __init__(self, adjacency):
        """
        Initializes a half-edge structure for the given adjacency data.

        :adjacency:     Iterable of iterables representing adjacency data of
                        the graph.
        :returns:       None.
        """
        """
        Properties.
        """
        self._vertices = []
        self._edges = []


