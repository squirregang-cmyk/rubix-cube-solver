import copy

class Corner:
    def __init__(self, identity, orientation=0, face_colours=None):
        self.identity = identity
        self.orientation = orientation
        self.face_colours = face_colours

    def __repr__(self):
        return f"Corner(identity={self.identity}, orientation={self.orientation})"



class Edge: 
    def __init__(self, identity, orientation=0, face_colours=None):
        self.identity = identity
        self.orientation = orientation
        self.face_colours = face_colours

    def __repr__(self):
        return f"Edge(identity={self.identity}, orientation={self.orientation})"


class Centre:
    def __init__(self, identity):
        self.identity = identity

    def __repr__(self):
        return(f"Centre(identity={self.identity})")
    
        

class Cube:
    def __init__(self):

        self.corners = {
            "URF": Corner("WRG", face_colours={"U": "W", "R": "R", "F": "G"}),
            "ULF": Corner("WOG", face_colours={"U": "W", "L": "O", "F": "G"}),
            "DRF": Corner("YRG", face_colours={"D": "Y", "R": "R", "F": "G"}),
            "DLF": Corner("YOG", face_colours={"D": "Y", "L": "O", "F": "G"}),

            "URB": Corner("WRB", face_colours={"U": "W", "R": "R", "B": "B"}),
            "ULB": Corner("WOB", face_colours={"U": "W", "L": "O", "B": "B"}),
            "DRB": Corner("YRB", face_colours={"D": "Y", "R": "R", "B": "B"}),
            "DLB": Corner("YOB", face_colours={"D": "Y", "L": "O", "B": "B"})
        }

        # Edge slots
        self.edges = {
            "UF": Edge("WG", face_colours={"U": "W", "F": "G"}),
            "UL": Edge("WO", face_colours={"U": "W", "L": "O"}),
            "UB": Edge("WB", face_colours={"U": "W", "B": "B"}),
            "UR": Edge("WR", face_colours={"U": "W", "R": "R"}),

            "DF": Edge("YG", face_colours={"D": "Y", "F": "G"}),
            "DL": Edge("YO", face_colours={"D": "Y", "L": "O"}),
            "DB": Edge("YB", face_colours={"D": "Y", "B": "B"}),
            "DR": Edge("YR", face_colours={"D": "Y", "R": "R"}),

            "FR": Edge("GR", face_colours={"F": "G", "R": "R"}),
            "FL": Edge("GO", face_colours={"F": "G", "L": "O"}),
            "BL": Edge("BO", face_colours={"B": "B", "L": "O"}),
            "BR": Edge("BR", face_colours={"B": "B", "R": "R"})
        }

        self.centres = {
            "U" : Centre("W"),
            "F" : Centre("G"),
            "R" : Centre("R"),
            "L" : Centre("O"),
            "B" : Centre("B"),
            "D" : Centre("Y")
        }

    def __repr__(self):
        corners = "\n".join(
            f"  {slot}: {piece}" for slot, piece in self.corners.items()
        )
        edges = "\n".join(
            f"  {slot}: {piece}" for slot, piece in self.edges.items()
        )
        centres = "\n".join(
            f"  {slot}: {piece}" for slot, piece in self.centres.items()
        )
        return (
            "Corners:\n"
            f"{corners}\n\n"
            "Edges:\n"
            f"{edges}\n\n"
            "Centres:\n"
            f"{centres}"
        )
        
        

cube = Cube()
solved_cube = copy.deepcopy(cube)

def reset():
    global cube
    cube = copy.deepcopy(solved_cube)

def is_solved():
    for position in cube.corners:
        if cube.corners[position].identity != solved_cube.corners[position].identity:
            return False

        if cube.corners[position].orientation != solved_cube.corners[position].orientation:
            return False

    for position in cube.edges:
        if cube.edges[position].identity != solved_cube.edges[position].identity:
            return False

        if cube.edges[position].orientation != solved_cube.edges[position].orientation:
            return False

    for position in cube.centres:
        if cube.centres[position].identity != solved_cube.centres[position].identity:
            return False

    return True



# Define a function to cycle the corners on the R face

def rotate_corner_faces(corners, slots, face_map):
    for slot in slots:
        corner = corners[slot]
        corner.face_colours = {
            face_map.get(face, face): colour
            for face, colour in corner.face_colours.items()
        }


def rotate_edge_faces(edges, slots, face_map):
    for slot in slots:
        edge = edges[slot]
        edge.face_colours = {
            face_map.get(face, face): colour
            for face, colour in edge.face_colours.items()
        }


def corner_cycle_no_twist(corner1, corner2, corner3, corner4, face_map=None):
    corners = cube.corners
    slots = (corner1, corner2, corner3, corner4)
    temporary_corner = corners[corner1]
    corners[corner1] = corners[corner2]
    corners[corner2] = corners[corner3]
    corners[corner3] = corners[corner4]
    corners[corner4] = temporary_corner
    if face_map:
        rotate_corner_faces(corners, slots, face_map)

def corner_cycle_twist_clockwise(corner1, corner2, corner3, corner4, face_map=None):
    corners = cube.corners
    slots = (corner1, corner2, corner3, corner4)
    temporary_corner = corners[corner1]
    corners[corner1] = corners[corner2]
    corners[corner2] = corners[corner3]
    corners[corner3] = corners[corner4]
    corners[corner4] = temporary_corner
    if face_map:
        rotate_corner_faces(corners, slots, face_map)

    corners[corner1].orientation = (corners[corner1].orientation +1) % 3
    corners[corner2].orientation = (corners[corner2].orientation +2) % 3
    corners[corner3].orientation = (corners[corner3].orientation +1) % 3
    corners[corner4].orientation = (corners[corner4].orientation +2) % 3

def corner_cycle_twist_counter_clockwise(corner1, corner2, corner3, corner4, face_map=None):
    corners = cube.corners
    slots = (corner1, corner2, corner3, corner4)
    temporary_corner = corners[corner1]
    corners[corner1] = corners[corner2]
    corners[corner2] = corners[corner3]
    corners[corner3] = corners[corner4]
    corners[corner4] = temporary_corner
    if face_map:
        rotate_corner_faces(corners, slots, face_map)

    corners[corner1].orientation = (corners[corner1].orientation +1) % 3
    corners[corner2].orientation = (corners[corner2].orientation +2) % 3
    corners[corner3].orientation = (corners[corner3].orientation +1) % 3
    corners[corner4].orientation = (corners[corner4].orientation +2) % 3


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

"""
def corner_cycle_F(prime=False):
    if not prime:
        corner_cycle_twist_clockwise("URF", "ULF", "DLF", "DRF")
    else:
        corner_cycle_twist_counter_clockwise("URF", "DRF", "DLF", "ULF")
"""

def corner_cycle_F():
    corner_cycle_twist_clockwise("URF", "ULF", "DLF", "DRF")



def corner_cycle_F_prime():
    corner_cycle_twist_counter_clockwise("URF", "DRF", "DLF", "ULF")



def corner_cylce_B():
    corner_cycle_twist_clockwise("URB", "DRB", "DLB", "ULB")



def corner_cylce_B_prime():
    corner_cycle_twist_counter_clockwise("URB", "ULB", "DLB", "DRB")


def edge_cycle_no_twist(edge1, edge2, edge3, edge4, face_map=None):
    edges = cube.edges
    slots = (edge1, edge2, edge3, edge4)
    temporary_edge = edges[edge1]
    edges[edge1] = edges[edge2]
    edges[edge2] = edges[edge3]
    edges[edge3] = edges[edge4]
    edges[edge4] = temporary_edge
    if face_map:
        rotate_edge_faces(edges, slots, face_map)

def edge_cycle_twist_clockwise(edge1, edge2, edge3, edge4, face_map=None):
    edges = cube.edges
    slots = (edge1, edge2, edge3, edge4)
    temporary_edge = edges[edge1]
    edges[edge1] = edges[edge2]
    edges[edge2] = edges[edge3]
    edges[edge3] = edges[edge4]
    edges[edge4] = temporary_edge
    if face_map:
        rotate_edge_faces(edges, slots, face_map)

    edges[edge1].orientation = (edges[edge1].orientation + 1) %2
    edges[edge2].orientation = (edges[edge2].orientation + 0) %2
    edges[edge3].orientation = (edges[edge3].orientation + 1) %2
    edges[edge4].orientation = (edges[edge4].orientation + 0) %2

def edge_cycle_twist_counter_clockwise(edge1, edge2, edge3, edge4, face_map=None):
    edges = cube.edges
    slots = (edge1, edge2, edge3, edge4)
    temporary_edge = edges[edge1]
    edges[edge1] = edges[edge2]
    edges[edge2] = edges[edge3]
    edges[edge3] = edges[edge4]
    edges[edge4] = temporary_edge
    if face_map:
        rotate_edge_faces(edges, slots, face_map)

    edges[edge1].orientation = (edges[edge1].orientation + 0) %2
    edges[edge2].orientation = (edges[edge2].orientation + 1) %2
    edges[edge3].orientation = (edges[edge3].orientation + 0) %2
    edges[edge4].orientation = (edges[edge4].orientation + 1) %2


def edge_cycle_U():
    edge_cycle_no_twist("UF", "UR", "UB", "UL")



def edge_cycle_U_prime():
    edge_cycle_no_twist("UF", "UL", "UB", "UR")



def edge_cycle_D():
    edge_cycle_no_twist("DF", "DR", "DB", "DL")



def edge_cycle_D_prime():
    edge_cycle_no_twist("DF", "DL", "DB", "DR")



def edge_cycle_R():
    edge_cycle_no_twist("FR", "DR", "BR", "UR")



def edge_cycle_R_prime():
    edge_cycle_no_twist("FR", "UR", "BR", "DR")



def edge_cycle_L():
    edge_cycle_no_twist("FL", "UL", "BL", "DL")



def edge_cycle_L_prime():
    edge_cycle_no_twist("FL", "DL", "BL", "UL")



def edge_cycle_F():
    edge_cycle_twist_clockwise("UF", "FR", "DF", "FL")



def edge_cycle_F_prime():
    edge_cycle_twist_counter_clockwise("UF", "FL", "DF", "FR")



def edge_cylce_B():
    edge_cycle_twist_clockwise("UB", "BL", "DB", "BR")



def edge_cylce_B_prime():
    edge_cycle_twist_counter_clockwise("UB", "BR", "DB", "BL")




def move_U():
    corner_cycle_no_twist("URF", "URB", "ULB", "ULF", {"R": "F", "B": "R", "L": "B", "F": "L"})
    edge_cycle_no_twist("UF", "UR", "UB", "UL", {"R": "F", "B": "R", "L": "B", "F": "L"})
    

def move_U_prime():
    corner_cycle_no_twist("URF", "ULF", "ULB", "URB", {"F": "R", "R": "B", "B": "L", "L": "F"})
    edge_cycle_no_twist("UF", "UL", "UB", "UR", {"F": "R", "R": "B", "B": "L", "L": "F"})

    
def move_D():
    corner_cycle_no_twist("DRF", "DRB", "DLB", "DLF", {"R": "F", "F": "L", "L": "B", "B": "R"})
    edge_cycle_no_twist("DF", "DR", "DB", "DL", {"R": "F", "B": "R", "L": "B", "F": "L"})

    
def move_D_prime():
    corner_cycle_no_twist("DRF", "DLF", "DLB", "DRB", {"F": "R", "L": "F", "B": "L", "R": "B"})
    edge_cycle_no_twist("DF", "DL", "DB", "DR", {"F": "R", "R": "B", "B": "L", "L": "F"})

    
def move_R():
    corner_cycle_twist_clockwise("URF", "DRF", "DRB", "URB", {"F": "U", "U": "B", "B": "D", "D": "F"})
    edge_cycle_no_twist("FR", "DR", "BR", "UR", {"F": "U", "U": "B", "B": "D", "D": "F"})
    

def move_R_prime():
    corner_cycle_twist_counter_clockwise("URF", "URB", "DRB", "DRF", {"U": "F", "F": "D", "D": "B", "B": "U"})
    edge_cycle_no_twist("FR", "UR", "BR", "DR", {"U": "F", "F": "D", "D": "B", "B": "U"})

    
def move_L():
    corner_cycle_twist_clockwise("ULF", "ULB", "DLB", "DLF", {"U": "F", "F": "D", "D": "B", "B": "U"})
    edge_cycle_no_twist("FL", "UL", "BL", "DL", {"U": "F", "F": "D", "D": "B", "B": "U"})

    
def move_L_prime():
    corner_cycle_twist_counter_clockwise("ULF", "DLF", "DLB", "ULB", {"F": "U", "U": "B", "B": "D", "D": "F"})
    edge_cycle_no_twist("FL", "DL", "BL", "UL", {"F": "U", "U": "B", "B": "D", "D": "F"})
    

def move_F():
    corner_cycle_twist_clockwise("URF", "ULF", "DLF", "DRF", {"U": "R", "R": "D", "D": "L", "L": "U"})
    edge_cycle_twist_counter_clockwise("UF", "FL", "DF", "FR", {"U": "R", "R": "D", "D": "L", "L": "U"})

    
def move_F_prime():
    corner_cycle_twist_counter_clockwise("URF", "DRF", "DLF", "ULF", {"R": "U", "U": "L", "L": "D", "D": "R"})
    edge_cycle_twist_clockwise("UF", "FR", "DF", "FL", {"R": "U", "U": "L", "L": "D", "D": "R"})


def move_B():
    corner_cycle_twist_clockwise("URB", "DRB", "DLB", "ULB", {"D": "R", "R": "U", "U": "L", "L": "D"})
    edge_cycle_twist_counter_clockwise("UB", "BR", "DB", "BL", {"U": "L", "R": "U", "D": "R", "L": "D"})


def move_B_prime():
    corner_cycle_twist_counter_clockwise("URB", "ULB", "DLB", "DRB", {"L": "U", "U": "R", "R": "D", "D": "L"})
    edge_cycle_twist_clockwise("UB", "BL", "DB", "BR", {"L": "U", "D": "L", "R": "D", "U": "R"})

