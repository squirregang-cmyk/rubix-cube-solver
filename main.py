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


class centre:
    def __init__(self, identity):
        self.identity = identity
    
        

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

        self.centres = {
            "U" : centre("W"),
            "F" : centre("G"),
            "R" : centre("R"),
            "L" : centre("O"),
            "B" : centre("B"),
            "D" : centre("Y")
        }
        

cube = Cube()

# Define a function to cycle the corners on the R face

def corner_cycle_no_twist(corner1, corner2, corner3, corner4):
    corners = cube.corners
    temporary_corner = corners[corner1]
    corners[corner1] = corners[corner2]
    corners[corner2] = corners[corner3]
    corners[corner3] = corners[corner4]
    corners[corner4] = temporary_corner

def corner_cycle_twist_clockwise(corner1, corner2, corner3, corner4):
    corners = cube.corners
    temporary_corner = corners[corner1]
    corners[corner1] = corners[corner2]
    corners[corner2] = corners[corner3]
    corners[corner3] = corners[corner4]
    corners[corner4] = temporary_corner

    corners[corner1].orientation = (corners[corner1].orientation +1) % 3
    corners[corner2].orientation = (corners[corner2].orientation +2) % 3
    corners[corner3].orientation = (corners[corner3].orientation +1) % 3
    corners[corner4].orientation = (corners[corner4].orientation +2) % 3

def corner_cycle_twist_counter_clockwise(corner1, corner2, corner3, corner4):
    corners = cube.corners
    temporary_corner = corners[corner1]
    corners[corner1] = corners[corner2]
    corners[corner2] = corners[corner3]
    corners[corner3] = corners[corner4]
    corners[corner4] = temporary_corner

    corners[corner1].orientation = (corners[corner1].orientation +2) % 3
    corners[corner2].orientation = (corners[corner2].orientation +1) % 3
    corners[corner3].orientation = (corners[corner3].orientation +2) % 3
    corners[corner4].orientation = (corners[corner4].orientation +1) % 3


def corner_cycle_U():
    corner_cycle_no_twist("URF", "URB", "ULB", "ULF")



def corner_cycle_U_prime():
    corner_cycle_no_twist("URF", "ULF", "ULB", "URB")



def corner_cycle_D():
    corner_cycle_no_twist("DRF", "DRB", "DLB", "DLF")



def corner_cycle_D_prime():
    corner_cycle_no_twist("DRF", "DLF", "DLB", "DRB")



def corner_cycle_R():
    corner_cycle_twist_clockwise("URF", "DRF", "DRB", "URB")



def corner_cycle_R_prime():
    corner_cycle_twist_counter_clockwise("URF", "URB", "DRB", "DRF")



def corner_cycle_L():
    corner_cycle_twist_clockwise("ULF", "ULB", "DLB", "DLF")



def corner_cycle_L_prime():
    corner_cycle_twist_counter_clockwise("ULF", "DLF", "DLB", "ULB")



def corner_cycle_F():
    corner_cycle_twist_clockwise("URF", "ULF", "DLF", "DRF")



def corner_cycle_F_prime():
    corner_cycle_twist_counter_clockwise("URF", "DRF", "DLF", "ULF")



def corner_cylce_B():
    corner_cycle_twist_clockwise("URB", "DRB", "DLB", "ULB")



def corner_cylce_B_prime():
    corner_cycle_twist_counter_clockwise("URB", "ULB", "DLB", "DRB")


#tests to see if cycles work on specific slots   
             
for n in range(4): 
    corner_cycle_U()
    print(cube.corners["URF"])
    n = n+1

    