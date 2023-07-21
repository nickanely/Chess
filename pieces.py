blackIcons = {"Pawn": "♙", "Rook": "♖", "Knight": "♘", "Bishop": "♗", "King": "♔", "Queen": "♕"}
whiteIcons = {"Pawn": "♟", "Rook": "♜", "Knight": "♞", "Bishop": "♝", "King": "♚", "Queen": "♛"}


class Piece:

    def __init__(self, color, board, position):
        self._color = color
        self._position = position
        self.__board = board

    @property
    def color(self):
        return self._color

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, move):
        self._position = move

    def validTup(self, move):
        if len(move) == 2:
            if (64 < ord(move[0]) < 73) or (96 < ord(move[0]) < 105):
                if 0 < int(move[1]) < 9:
                    return True
        return False

    def checkMove(self, dest):
        return False

    def move(self, dest):
        if self.checkMove(dest):
            self.__board.update(self.position, dest)
            self.position = dest
        return False

    def getName(self):
        return "pieces"

    def getIcon(self):
        name = self.getName()
        color = self.color
        if color == "white":
            return whiteIcons[name]
        else:
            return blackIcons[name]


class Knight(Piece):
    def getName(self):
        return "Knight"

    def move(self, dest):
        if self.checkMove(dest):
            return super().move(dest)
        return False

    def checkMove(self, dest):
        post = self.position
        p1 = ord(post[0])
        p2 = int(post[1])
        d1 = ord(dest[0])
        d2 = int(dest[1])
        if post == dest:
            return False
        else:
            if (d1 in range(65, 73)) and (d2 in range(1, 9)):
                if (p1 + 1 == d1) or (p1 - 1 == d1):
                    if (p2 + 2 == d2) or (p2 - 2 == d2):
                        return True
                elif (p1 + 2 == d1) or (p1 - 2 == d1):
                    if (p2 + 1 == d2) or (p2 - 1 == d2):
                        return True
            return False

class Rook(Piece):
    def getName(self):
        return "Rook"

    def move(self, dest):
        if self.checkMove(dest):
            return super().move(dest)
        return False

    def checkMove(self, dest):
        post = self.position
        p1 = ord(post[0])
        p2 = post[1]
        d1 = ord(dest[0])
        d2 = dest[1]
        if post == dest:
            return False
        else:
            if (d1 in range(65, 73)) and (d2 in range(1, 9)):
                if (p1 == d1) and (p2 != d2):
                    return True
                elif (p2 == d2) and (p1 != d1):
                    return True
            return False


class Bishop(Piece):
    def getName(self):
        return "Bishop"

    def move(self, dest):
        if self.checkMove(dest):
            return super().move(dest)
        return False

    def checkMove(self, dest):
        post = self.position
        c = self.color()
        p1 = ord(post[0])
        p2 = int(post[1])
        d1 = ord(dest[0])
        d2 = int(dest[1])
        X = abs(p1 - d1)
        Z = abs(p2 - d2)
        if post == dest:
            return False
        else:
            if X == Z:
                return True
            else:
                return False


class Queen(Piece):
    def getName(self):
        return "Queen"

    def move(self, dest):
        if self.checkMove(dest):
            return super().move(dest)
        return False

    def checkMove(self, dest):
        post = self._position
        p1 = ord(post[0])
        p2 = int(post[1])
        d1 = ord(dest[0])
        d2 = int(dest[1])
        X = abs(p1 - d1)
        Z = abs(p2 - d2)
        if post == dest:
            return False
        else:
            if X == Z:
                return True
            elif (d1 in range(65, 73)) and (d2 in range(1, 9)):
                if (p1 == d1) and (p2 != d2):
                    return True
                elif (p2 == d2) and (p1 != d1):
                    return True
        return False


class King(Piece):
    def getName(self):
        return "King"

    def move(self, dest):
        if self.checkMove(dest):
            return super().move(dest)
        return False

    def checkMove(self, dest):
        post = self.position
        c = self.color()
        p1 = ord(post[0])
        p2 = int(post[1])
        d1 = ord(dest[0])
        d2 = int(dest[1])
        if post == dest:
            return False
        else:
            if (d1 in range(65, 73)) and (d2 in range(1, 9)):
                if (p1 == d1) or (p1 + 1 == d1) or (p1 - 1 == d1):
                    if (p2 == d2) or (p2 + 1 == d1) or (p2 - 1 == d2):
                        return True
            return False


class Pawn(Piece):
    def getName(self):
        return "Pawn"

    def move(self, dest):
        if self.checkMove(dest):
            return super().move(dest)
        return False


    def checkMove(self, dest):
        post = self.position
        c = self._color
        p1 = ord(post[0])
        p2 = int(post[1])
        d1 = ord(dest[0])
        d2 = int(dest[1])
        if post == dest:
            return False
        else:
            if (d1 in range(65, 73)) and (d2 in range(1, 9)):
                if c == "White":
                    if p1 == d1:
                        if p2 == d2 - 1:
                            return True
                elif c == "Black":
                    if p1 == d1:
                        if p2 == d2+1:
                            return True

            return False
