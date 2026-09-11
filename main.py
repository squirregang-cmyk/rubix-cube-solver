import random
from PySide6 import QtCore, QtWidgets, QtGui
import sys
import cube_functions

#tests to see if cycles work on specific slots   


"""
for n in range(4): 
    cube_functions.move_U()
    print(cube.corners["URF"])
    print(cube.edges["UF"])
    n = n+1
"""

move_notation = {
    cube_functions.move_U : "U", cube_functions.move_U_prime : "U'",
    cube_functions.move_D : "D", cube_functions.move_D_prime : "D'",
    cube_functions.move_R : "R", cube_functions.move_R_prime : "R'",
    cube_functions.move_L : "L", cube_functions.move_L_prime : "L'",
    cube_functions.move_F : "F", cube_functions.move_F_prime : "F'",
    cube_functions.move_B : "B", cube_functions.move_B_prime : "B'",
}
All_moves = list(move_notation.keys())

#flips the key and values around from the first dictionary, so that the list from the scramble can be turned into usable moves
string_to_move = { string: func for func, string in move_notation.items() }
scramble_list = []

def generate_random_moves(scramble_length):
    scramble_list.clear()

    for i in range(scramble_length):
        chosen_move = random.choice(All_moves)


        clean_name = move_notation[chosen_move]
        scramble_list.append(clean_name)
    print(f"Scramble: {' '.join(scramble_list)}")
    
    return scramble_list

def apply_moves_to_cube(scramble_list):

    for move_letter in scramble_list:
        actual_move_function = string_to_move[move_letter]

        actual_move_function()


#need to make dicitonary to map old 3d peices into their respective stickers/sides


corner_stickers = {
    "URF": ["U9", "R1", "F3"],
    "ULF": ["U7", "L3", "F1"],
    "URB": ["U3", "R3", "B1"],
    "ULB": ["U1", "L1", "B3"],

    "DRF": ["D3", "R7", "F9"],
    "DLF": ["D1", "L9", "F7"],
    "DRB": ["D9", "R9", "B7"],
    "DLB": ["D7", "L7", "B9"],
}

edge_stickers = {
    "UF": ["U8", "F2"],
    "UR": ["U6", "R2"],
    "UB": ["U2", "B2"],
    "UL": ["U4", "L2"],

    "DF": ["D2", "F8"],
    "DR": ["D6", "R8"],
    "DB": ["D8", "B8"],
    "DL": ["D4", "L8"],

    "FR": ["F6", "R4"],
    "FL": ["F4", "L6"],
    "BR": ["B6", "R6"],
    "BL": ["B4", "L4"],
}

centre_stickers = {
    "U": ["U5"],
    "F": ["F5"],
    "R": ["R5"],
    "L": ["L5"],
    "B": ["B5"],
    "D": ["D5"],
}

stickers = {
    # U face
    "U1": "W",
    "U2": "W",
    "U3": "W",
    "U4": "W",
    "U5": "W",
    "U6": "W",
    "U7": "W",
    "U8": "W",
    "U9": "W",

    # F face
    "F1": "G",
    "F2": "G",
    "F3": "G",
    "F4": "G",
    "F5": "G",
    "F6": "G",
    "F7": "G",
    "F8": "G",
    "F9": "G",

    # R face
    "R1": "R",
    "R2": "R",
    "R3": "R",
    "R4": "R",
    "R5": "R",
    "R6": "R",
    "R7": "R",
    "R8": "R",
    "R9": "R",

    # L face
    "L1": "O",
    "L2": "O",
    "L3": "O",
    "L4": "O",
    "L5": "O",
    "L6": "O",
    "L7": "O",
    "L8": "O",
    "L9": "O",

    # B face
    "B1": "B",
    "B2": "B",
    "B3": "B",
    "B4": "B",
    "B5": "B",
    "B6": "B",
    "B7": "B",
    "B8": "B",
    "B9": "B",

    # D face
    "D1": "Y",
    "D2": "Y",
    "D3": "Y",
    "D4": "Y",
    "D5": "Y",
    "D6": "Y",
    "D7": "Y",
    "D8": "Y",
    "D9": "Y",
}


def colour_assignment(peice_for_assignment):

    #checks the dictionary 
    if peice_for_assignment in corner_stickers:

        corner = cube_functions.cube.corners[peice_for_assignment]

        orientation = corner.orientation

        colour1, colour2, colour3 = corner.identity

        if orientation == 1:
            colour1, colour2, colour3 = colour2, colour3, colour1

        elif orientation == 2:
            colour1, colour2, colour3 = colour3, colour1, colour2

        positions = corner_stickers[peice_for_assignment]

        stickers[positions[0]] = colour1
        stickers[positions[1]] = colour2
        stickers[positions[2]] = colour3
    
    #checks dicitonary
    elif peice_for_assignment in edge_stickers:

        edge = cube_functions.cube.edges[peice_for_assignment]

        orientation = edge.orientation

        colour1, colour2 = edge.identity

        if orientation == 1:
            colour1, colour2 = colour2, colour1

        positions = edge_stickers[peice_for_assignment]
        
        stickers[positions[0]] = colour1
        stickers[positions[1]] = colour2

    else:

        centre = cube_functions.cube.centres[peice_for_assignment]

        colour1 = centre.identity

        positions = centre_stickers[peice_for_assignment]

        stickers[positions[0]] = colour1

def update_all_stickers():

    for position in corner_stickers:
        colour_assignment(position)

    for position in edge_stickers:
        colour_assignment(position)

    for position in centre_stickers:
        colour_assignment(position)


#goes through all positions of stickers on cube and checks what value is held in the dictionary and then uses that to assign the colour
def update_sticker(sticker_key, square):

    colour = stickers[sticker_key]

    if colour == "W":
        square.setStyleSheet("background-color: white;")

    elif colour == "Y":
        square.setStyleSheet("background-color: yellow;")

    elif colour == "R":
        square.setStyleSheet("background-color: red;")

    elif colour == "O":
        square.setStyleSheet("background-color: orange;")

    elif colour == "G":
        square.setStyleSheet("background-color: green;")

    elif colour == "B":
        square.setStyleSheet("background-color: blue;")


#will work on cube net later, dont understand and ai confused me with it
"""
class CubeNet(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        layout = QtWidgets.QGridLayout(self)

        # Create the 54 squares
        self.stickers = {}

        faces = ["U", "L", "F", "R", "B", "D"]

        for face in faces:
            for number in range(1, 10):
                key = f"{face}{number}"

                square = QtWidgets.QLabel()
                square.setFixedSize(50, 50)
                square.setStyleSheet(
                    "background-color: white; border: 1px solid black;"
                )

                self.stickers[key] = square
"""



class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.scramble_title = QtWidgets.QLabel("Scramble", )
        self.scramble_text = QtWidgets.QLabel(f"{' '.join(scramble_list)}")
        self.scramble_button = QtWidgets.QPushButton("Scramble")
        self.reset_button = QtWidgets.QPushButton("Reset")
        
        
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.scramble_title, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.scramble_text, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        
        
                
        button_layout = QtWidgets.QHBoxLayout()
        
        
        self.layout.addLayout(button_layout)
                
                
        
        self.scramble_button.clicked.connect(self.magic)
        self.reset_button.clicked.connect(self.reset_scramble_and_cube)
        

        self.sticker_widgets = {}
        cube_layout = self.create_cube_net()
        self.layout.addLayout(cube_layout)

        self.update_cube_display()

        button_layout.addWidget(self.scramble_button)
        button_layout.addWidget(self.reset_button)

        self.layout.addStretch()

    def update_cube_display(self):

        update_all_stickers()

        for sticker_key, square in self.sticker_widgets.items():
            update_sticker(sticker_key, square)

    def create_cube_net(self):

        cube_layout = QtWidgets.QGridLayout()
        cube_layout.setSpacing(0)

        cube_layout.setContentsMargins(0, 0, 0, 0)
        cube_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)

        faces = {
            "U" : (0,1),
            "L" : (1,0), 
            "F" : (1,1), 
            "R" : (1,2),
            "B" : (1,3),
            "D" : (2,1)
        }

        for i in range(12):
            cube_layout.setColumnStretch(i, 0)

        for i in range(9):
            cube_layout.setRowStretch(i, 0)

        for face, (face_row, face_col) in faces.items():

            for row in range(3):
                for col in range(3):

                    number = row * 3 + col + 1
                    sticker_key = f"{face}{number}"

                    square = QtWidgets.QLabel()
                    square.setAlignment(QtCore.Qt.AlignCenter)
                    square.setFixedSize(35, 35)

                    square.setStyleSheet(
                        "background-color: white;"
                        "border: 0px;"
                    )

                    cube_layout.addWidget(
                        square,
                        face_row * 3 + row,
                        face_col * 3 + col
                    )

                    self.sticker_widgets[sticker_key] = square

        cube_layout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        return cube_layout


    @QtCore.Slot()

    def reset_scramble_and_cube(self):
        cube_functions.reset()
        print(cube_functions.cube)
        self.scramble_text.setText("")

        self.update_cube_display()
        

    def magic(self):
        #self.text.setText(random.choice(self.hello))

        scramble_length = random.randint(20, 25) #int(input("enter a numer: "))
        #scramble_length = random.randint(1, 35)

        generate_random_moves(scramble_length)
        apply_moves_to_cube(scramble_list)

        print(cube_functions.cube)
        #print(cube.corners["URF"])
        #print(cube.edges["UF"])
        self.scramble_text.setText(f"{' '.join(scramble_list)}")

        self.update_cube_display()  


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())