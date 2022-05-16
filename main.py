from mm import minimax_pruning
from score import calcScore
import chess

# Prompts the player to enter their move and then pushes the move to the board
def player_move(board):
    rank = ['1', '2', '3', '4', '5', '6', '7', '8']
    file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    legal_moves = board.generate_legal_moves()
    pm = input('Move (ex: e2e4): ')
    move = chess.Move.from_uci(str(pm))
    if not (move in legal_moves):
        print('Please enter a legal move!')
        return player_move(board)
    board.push(move)
    return board


# Runs the minimax algorithm and pushes the optimal move to the board
def comp_move(board, depth):
    print('Thinking...')

    moves = [str(i) for i in board.legal_moves]
    l = []
    for move in moves:
        board.push(chess.Move.from_uci(move))
        l.append(minimax_pruning(board, 3, -10000000000, 100000000000000, False))
        board.pop()
    best = moves[l.index(min(l))]
    board.push(chess.Move.from_uci(best))
    print('Best Move: ' + str(best))
    return board


board = chess.Board()

print(board)
print()
print(calcScore(board))

while not board.is_checkmate():
    board = player_move(board)
    print(board)
    print(calcScore(board))
    print()
    board = comp_move(board, 3)
    print(board)
    print(calcScore(board))
    print()