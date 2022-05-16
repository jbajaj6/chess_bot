import chess
from mm import minimax, minimax_pruning
import time
from score import calcScore

t = time.time()

board = chess.Board()

print(board)

print()
for i in range(100):

    isEven = True if i%2==0 else False

    moves = [str(i) for i in board.legal_moves]
    l = []
    for move in moves:
        board.push(chess.Move.from_uci(move))
        l.append(minimax_pruning(board, 3, -10000000000, 100000000000000, isEven))
        board.pop()
    if isEven:
        best = moves[l.index(max(l))]
        board.push(chess.Move.from_uci(best))
        print(best)
    else:
        best = moves[l.index(min(l))]
        board.push(chess.Move.from_uci(best))
        print(best)
    print(board)
    print()
    print(calcScore(board))
    print()

elapsed = time.time() - t

print(f"Time: {elapsed}")
print(f"Avg time per move: {elapsed/100}")