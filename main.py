import random
from PySide6 import QtCore, QtWidgets, QtGui
import sys
import cube_functions

#tests to see if cycles work on specific slots   

cube = cube_functions.cube 

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

        self.layout.addStretch()
        
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.scramble_button)
        button_layout.addWidget(self.reset_button)

        self.layout.addLayout(button_layout)
        
        

        self.scramble_button.clicked.connect(self.magic)
        self.reset_button.clicked.connect(self.reset_scramble_and_cube)

    @QtCore.Slot()

    def reset_scramble_and_cube(self):
        cube_functions.reset()
        print(cube_functions.cube)
        self.scramble_text.setText("")
        

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


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())