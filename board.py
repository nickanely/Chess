from pieces import *


class Board:
    def __init__(self):
        self.board = [['8', "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                      ['7', "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                      ['6', "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                      ['5', "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                      ['4', "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                      ['3', "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                      ['2', "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                      ['1', "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]", "[ ]"],
                      [' ', "A", 'B', 'C', 'D', ' E', ' F', 'G', 'H']]

    def placePieces(self):
        self.board[6][1] = Pawn("White", self, "A2")
        self.board[6][2] = Pawn("White", self, "B2")
        self.board[6][3] = Pawn("White", self, "C2")
        self.board[6][4] = Pawn("White", self, "D2")
        self.board[6][5] = Pawn("White", self, "E2")
        self.board[6][6] = Pawn("White", self, "F2")
        self.board[6][7] = Pawn("White", self, "G2")
        self.board[6][8] = Pawn("White", self, "H2")

        self.board[1][1] = Pawn("Black", self, "A7")
        self.board[1][2] = Pawn("Black", self, "B7")
        self.board[1][3] = Pawn("Black", self, "C7")
        self.board[1][4] = Pawn("Black", self, "D7")
        self.board[1][5] = Pawn("Black", self, "E7")
        self.board[1][6] = Pawn("Black", self, "F7")
        self.board[1][7] = Pawn("Black", self, "G7")
        self.board[1][8] = Pawn("Black", self, "H7")

        self.board[7][1] = Rook("White", self, "A1")
        self.board[7][2] = Knight("White", self, "B1")
        self.board[7][3] = Bishop("White", self, "C1")
        self.board[7][4] = Queen("White", self, "D1")
        self.board[7][5] = King("White", self, "E1")
        self.board[7][6] = Bishop("White", self, "F1")
        self.board[7][7] = Knight("White", self, "G1")
        self.board[7][8] = Rook("White", self, "H1")

        self.board[0][1] = Rook("Black", self, "A8")
        self.board[0][2] = Knight("Black", self, "B8")
        self.board[0][3] = Bishop("Black", self, "C8")
        self.board[0][4] = Queen("Black", self, "D8")
        self.board[0][5] = King("Black", self, "E8")
        self.board[0][6] = Bishop("Black", self, "F8")
        self.board[0][7] = Knight("Black", self, "G8")
        self.board[0][8] = Rook("Black", self, "H8")

    blackIcons = {"Pawn": "♙", "Rook": "♖", "Knight": "♘", "Bishop": "♗", "King": "♔", "Queen": "♕"}
    whiteIcons = {"Pawn": "♟", "Rook": "♜", "Knight": "♞", "Bishop": "♝", "King": "♚", "Queen": "♛"}

    def setPiece(self, position, piece):
        self.board[8 - int(position[1])][ord(position[0])-64] = piece

    def validTup(self, move):
        if len(move) == 2:
            if (64 < ord(move[0]) < 73) or (96 < ord(move[0]) < 105):
                if 0 < int(move[1]) < 9:
                    return True
        return False

    def tuplToPlc(self, position):
        if self.validTup(position):
            alphabet = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
            f = alphabet[position[0]]
            s = 8 - int(position[1])
            tp = (s, f)
            return tp

    def getPiece(self, position):
        return self.board[8 - int(position[1])][ord(position[0])-64]


    def makeMove(self, startPosition, endPosition, player):
        tup_p = self.tuplToPlc(startPosition)
        tup_s = self.tuplToPlc(endPosition)
        p = self.getPiece(startPosition).color if self.getPiece(startPosition) else print("h")
        s = self.getPiece(endPosition).color if self.getPiece(endPosition) else print("h")
        if p == s or not not s:
            print("cannot make this move")
        elif p != player:
            print("Make a move with your piece")
        elif p == player:
            self.board[tup_s[0]][tup_s[1]] = self.getPiece(startPosition)
            self.board[tup_s[0]][tup_s[1]].move(endPosition)
            self.board[tup_p[0]][tup_p[1]] = "[ ]"

    def displayBoard(self):
        for i in range(len(self.board)):
            for j in self.board[i]:
                if type(j) == str:
                    print(j, end=" ")
                else:
                    print(j.getIcon(), end=" ")
            print()

    def update(self, a, b):
        x = self.board[8 - int(a[1])][ord(a[0]) - 64]
        self.board[8 - int(b[1])][ord(b[0]) - 64] = x
        self.board[8 - int(a[1])][ord(a[0]) - 64] = "[ ]"

