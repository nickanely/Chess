from board import *
from pieces import *


class Chess(Board, Piece):
    def __init__(self):
        self.cur_player = "White"
        self._board = Board()

    def promotion(self):
        t = True
        if "♟" in self._board.board[0]:
            while t:
                p = input("pawn promoted. Choose the piece!")
                if p in whiteIcons:
                    newp = whiteIcons[p]
                    for x in range(1, 9):
                        if self._board.board[0][x] == "♟":
                            self._board.board[0][x] = newp
                        t = False
                else:
                    t = True
        elif "♙" in self._board.board[7]:
            while t:
                p = input("pawn promoted. Choose the piece!")
                if p in blackIcons:
                    newp = blackIcons[p]
                    for x in range(1, 9):
                        if self._board.board[7][x] == "♙":
                            self._board.board[7][x] = newp
                        t = False
                else:
                    t = True
        else:
            return False

    def swapPlayers(self):
        if self.cur_player == "White":
            self.cur_player = "Black"
        else:
            self.cur_player = "White"

    def isStringValid(self, moveStr):
        if len(moveStr) == 5:
            if ord(moveStr[0]) in range(65, 73):
                if ord(moveStr[1]) in range(49, 57):
                    if moveStr[2] == ' ':
                        if ord(moveStr[3]) in range(65, 73):
                            if ord(moveStr[4]) in range(49, 57):
                                return True
        return False

    def translatordest(self, inp):
        return inp[3:]

    def translatorpost(self, inp):
        return inp[0:2]

    def play(self):

        self._board.placePieces()
        while 1:
            self._board.displayBoard()
            player = self.cur_player
            while 1:
                inp = input(f"{self.cur_player} make a move")
                if inp == "EXIT":
                    print("The end")
                    return
                elif self.isStringValid(inp):
                    post = self.translatorpost(inp)
                    dest = self.translatordest(inp)
                    mp = self._board.getPiece(post)
                    if type(mp) == str:
                        pass
                    elif mp.checkMove(dest):
                        mp.move(dest)
                        break
                    else:
                        print("move cannot be done")
            self.swapPlayers()

        # self.promotion()
        self.displayBoard()



if __name__ == "__main__":
    game = Chess()
    game.play()
