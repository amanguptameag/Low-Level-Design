from enum import Enum
from typing import List

class Chess:
    def __init__(self):
        self.chessBoard: ChessBoard
        self.current_player: Player
        self.game_status: GameStatus
        self.players: List[Player]
        self.moves_list: List[Move]

    def player_move(self, from_position: CellPosition, to_position: CellPosition, piece: Piece):
        pass

    def end_game(self):
        pass

    def __change_turn(self):
        pass


class Player:
    def __init__(self):
        self.account: Account
        self.color: Color
        self.time_left: Time


class Account:
    def __init__(self):
        self.username: str
        self.password: str
        self.name: str
        self.email: str
        self.phone: str


class Color(Enum):
    BLACK = 0
    WHITE = 1

class Time:
    def __init__(self):
        self.mins: int
        self.secs: int

class GameStatus(Enum):
    ACTIVE = 0
    PAUSED = 1
    BLACK_WIN = 2
    WHITE_WIN = 3


class ChessBoard:
    def __init__(self):
        self.board: List[List[Cell]]

    def reset_board(self):
        pass

    def update_board(self, move: Move):
        pass

class Cell:
    def __init__(self):
        self.color: Color
        self.piece: Piece
        self.cell_position: CellPosition

class CellPosition:
    def __init__(self):
        self.ch: str
        self.i: int

class Move:
    def __init__(self):
        self.turn: Player
        self.piece: Piece
        self.killed_piece: Piece
        self.start_position: CellPosition
        self.end_position: CellPosition

class Piece:
    def __init__(self):
        self.color: Color

    def move(self, from_position: CellPosition, to_position: CellPosition):
        pass

    def possible_moves(self, from_position: CellPosition):
        pass

    def validate(self, from_position: CellPosition, to_position: CellPosition):
        pass