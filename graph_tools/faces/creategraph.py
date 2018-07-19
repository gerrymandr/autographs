
import pysal as ps


def rook(path):
    """
    Generates a rook-adjacency dual graph from a shapefile.
    
    :path:      Path to shapefile.
    :returns:   Rook-adjacency of the units in the shapefile.
    """
    return ps.weights.Rook.from_shapefile(path)


def queen(path):
    """
    Generates a queen-adjacency dual graph from a shapefile.

    :path:      Path to shapefile.
    :returns:   Queen-adjacency of the units in the shapefile.
    """
    return ps.weights.Queen.from_shapefile(path)


if __name__ == "__main__":
    rook = rook("../../test/data/tl_2016_19_cousub/tl_2016_19_cousub.shp")
    print(rook[0])
