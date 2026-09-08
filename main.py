class Corner:
    def __init__(self, identity, orientation = 0):
        self.identity = identity
        self.orientation = orientation

    def __repr__(self):
        return f"Corner(identity={self.identity}, orientation={self.orientation})"



class Edge: 
    def __init__(self, identity, orientation = 0):
        self.identity = identity
        self.orientation = orientation

    def __repr__(self):
        return f"Edge(identity={self.identity}, orientation={self.orientation})"
        

class Cube:
    def __init__(self):

        self.corners = {
            "URF": Corner("WRG"),
            "ULF": Corner("WOG"),
            "DRF": Corner("YRG"),
            "DLF": Corner("YOG"),

            "URB": Corner("WRB"),
            "ULB": Corner("WOB"),
            "DRB": Corner("YRB"),
            "DLB": Corner("YOB")
        }

        # Edge slots
        self.edges = {
            "UF": Edge("WG"),
            "UL": Edge("WO"),
            "UB": Edge("WB"),
            "UR": Edge("WR"),

            "DF": Edge("YG"),
            "DL": Edge("YO"),
            "DB": Edge("YB"),
            "DR": Edge("YR"),

            "FR": Edge("GR"),
            "FL": Edge("GO"),
            "BL": Edge("BO"),
            "BR": Edge("BR")
        }

cube = Cube()
print(cube.corners["URF"])

# Define a function to cycle the corners on the R face

def corner_cycle_R():
    corners = cube.corners
    temporary_corner = corners["URF"]
    corners["URF"] = corners["DRF"]
    corners["DRF"] = corners["DRB"]
    corners["DRB"] = corners["URB"]
    corners["URB"] = temporary_corner

    corners["URF"].orientation = (corners["URF"].orientation + 1) % 3
    corners["DRF"].orientation = (corners["DRF"].orientation + 1) % 3
    corners["DRB"].orientation = (corners["DRB"].orientation + 1) % 3
    corners["URB"].orientation = (corners["URB"].orientation + 1) % 3

#test to see if the corner cycle works
#corner_cycle_R()
#print(cube.corners["URF"])
#corner_cycle_R()
#print(cube.corners["URF"])

def corner_cycle_L():
    corners = cube.corners
    temporary_corner = corners["ULF"]
    corners["ULF"] = corners["ULB"]
    corners["ULB"] = corners["DLB"]
    corners["DLB"] = corners["DLF"]
    corners["DLF"] = temporary_corner

    corners["ULF"].orientation = (corners["ULF"].orientation + 1) % 3
    corners["ULB"].orientation = (corners["ULB"].orientation + 1) % 3
    corners["DLB"].orientation = (corners["DLB"].orientation + 1) % 3
    corners["ULF"].orientation = (corners["ULF"].orientation + 1) % 3

    