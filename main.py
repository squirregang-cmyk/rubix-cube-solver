import random
from pySide6 import QtCore, QtCore, QtWidgets, QtGui
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

scramble_length = int(input("enter a numer"))
scramble_list = []

def generate_random_moves(scramble_length):

    for i in range(scramble_length):
        chosen_move = random.choice(All_moves)


        clean_name = move_notation[chosen_move]
        scramble_list.append(clean_name)
    print(f"Scramble: {' '.join(scramble_list)}")
    
    return scramble_list

generate_random_moves(scramble_length)
print(scramble_list)

def apply_moves_to_cube(scramble_list):

    for move_letter in scramble_list:
        actual_move_function = string_to_move[move_letter]

        actual_move_function()



apply_moves_to_cube(scramble_list)

print(cube.corners["URF"])
print(cube.edges["UF"])
