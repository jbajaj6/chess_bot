from score import calcScore
import chess

def minimax(board, depth, isMax):
    if board.is_checkmate():
        if isMax:
            return 9999999999999999999
        else:
            return -9999999999999999999

    if board.is_stalemate():
        return 0

    if(depth == 0):
        return calcScore(board)
    canMove = board.legal_moves
    if isMax:
        best = -999999999
        for i in canMove:
            move = chess.Move.from_uci(str(i))
            board.push(move)
            best = max(best, minimax(board, depth - 1, not isMax))
            board.pop()
        return best
    else:
        best = 999999999
        for x in canMove:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            best = min(best, minimax(board, depth - 1, not isMax))
            board.pop()
        return best

def minimax_pruning(board, depth, alpha, beta, isMax):
    if board.is_checkmate():
        if isMax:
            return 9999999999999999999
        else:
            return -9999999999999999999

    if board.is_stalemate():
        if isMax:
            return -999999
        else:
            return  999999

    if(depth == 0):
        return calcScore(board)
    canMove = board.legal_moves
    if isMax:
        best = -999999999
        for i in canMove:
            move = chess.Move.from_uci(str(i))
            board.push(move)
            eval = minimax_pruning(board, depth - 1,  alpha, beta, not isMax)
            best = max(best, eval)
            board.pop()
            alpha = max(alpha, eval) 
            if beta <= alpha:
                break
        return best
    else:
        best = 999999999
        for x in canMove:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            eval = minimax_pruning(board, depth - 1,  alpha, beta, not isMax)
            best = min(best, eval)
            board.pop()
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return best