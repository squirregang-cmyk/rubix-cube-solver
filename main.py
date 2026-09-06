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

print(Cube().corners["URF"])