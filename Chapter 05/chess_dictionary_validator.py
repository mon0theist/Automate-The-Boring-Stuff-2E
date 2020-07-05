#! /usr/bin/python
#
# ATBS2E - Chapter 5 - Chess Dictionary Validator
#
# In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen',
# '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board.
# Write a function named isValidChessBoard() that takes a dictionary argument
# and returns True or False depending on if the board is valid.
#
# A valid board will have exactly one black king and exactly one white king. Each
# player can only have at most 16 pieces, at most 8 pawns, and all pieces must
# be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'.
# The piece names begin with either a 'w' or 'b' to represent white or black,
# followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This
# function should detect when a bug has resulted in an improper chess board.

spaces = [
'1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a',
'1b', '2b', '3b', '4b', '5b', '6b', '7b', '8b',
'1c', '2c', '3c', '4c', '5c', '6c', '7c', '8c',
'1d', '2d', '3d', '4d', '5d', '6d', '7d', '8d',
'1e', '2e', '3e', '4e', '5e', '6e', '7e', '8e',
'1f', '2f', '3f', '4f', '5f', '6f', '7f', '8f',
'1g', '2g', '3g', '4g', '5g', '6g', '7g', '8g',
'1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h'
]

# Test Chess Boards
valid_board1 = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
valid_board2 = {'2h': 'wking', '5c': 'bqueen', '3g': 'wbishop', '6h': 'wqueen', '4e': 'bking'}
no_kings = {'5c': 'bqueen', '3g': 'wbishop', '6h': 'wqueen', '4e': 'bknight'}
one_king = {'1h': 'bknight', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
many_pawns = {'1e': 'wking', '8e': 'bking', '2a': 'wpawn', '2b': 'wpawn', '2c': 'wpawn', '2d': 'wpawn', '2e': 'wpawn', '2f': 'wpawn', '2g': 'wpawn', '2h': 'wpawn', '3a': 'wpawn'}
invalid_space = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5z': 'bqueen', '3e': 'wking'}
wrong_name = {'1h': 'bking', '6c': 'oqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessBoard(board_dict):
    # check for exactly one black king and one white king
    wkings = 0
    bkings = 0
    for piece in board_dict.values():
        if piece == 'wking':
            wkings += 1
        elif piece == 'bking':
            bkings += 1
    if wkings != 1 or bkings != 1:
        print('Invalid number of kings')
        return False

    # check for max of 16 pieces per player
    # and all pieces start with either 'w' or 'b'
    wplayer = 0
    bplayer = 0
    for piece in board_dict.values():
        if piece.startswith('w'):
            wplayer += 1
        elif piece.startswith('b'):
            bplayer += 1
        else:
            print('Invalid piece: ' + piece)
            return False
    if wplayer >= 17:
        print('Invalid: White has too many pieces')
        return False
    elif bplayer >= 17:
        print('Invalid: Black has too many pieces')
        return False

    # check for max of 8 pawns per player:
    wpawns = 0
    bpawns = 0
    for piece in board_dict.values():
        if 'wpawn' in board_dict.values():
            wpawns += 1
        elif 'bpawn' in board_dict.values():
            bpawns += 1
    if wpawns >= 9:
        print('Invalid: White has too many pawns')
        return False
    if bpawns >= 9:
        print('Invalid: Black has too many pawns')
        return False

    # check if all pieces are on a valid space
    for space in board_dict.keys():
        if space not in spaces:
            print('Invalid space: ' + space)
            return False

    # check for valid piece names
    pieces = [
    'wknight', 'wbishop', 'wrook', 'wqueen', 'wking', 'bknight', 'bbishop',
    'brook', 'bqueen', 'bking'
    ]
    for names in board_dict.values():
        if names not in pieces:
            print('Invalid piece: ' + names)
            return False

print('Validating test chess boards...')

print('Testing no_kings...')
isValidChessBoard(no_kings)

print('Testing one_kings...')
isValidChessBoard(one_king)

print('Testing many_pawns...')
isValidChessBoard(many_pawns)

print('Testing invalid_space...')
isValidChessBoard(invalid_space)

print('Testing wrong_name...')
isValidChessBoard(wrong_name)

print('Testing valid_board1...')
isValidChessBoard(valid_board1)

print('Testing valid_board2...')
isValidChessBoard(valid_board2)
