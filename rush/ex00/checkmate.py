#!/usr/bin/env python

def checkmate(*rows):
    board = [list(row) for row in rows]
    n = len(board)

    # King
    king = None
    for r in range(n):
        for c in range(n):
            if board[r][c] == "K":
                king = (r, c)
                break
        if king:
            break
    if not king:
        print("Fail")
        return

    kr, kc = king

    for r in range(n):
        for c in range(n):
            piece = board[r][c]
            if piece == "." or piece == "K":
                continue

            # Pawn 
            if piece == "P":
                for dr, dc in [(-1,-1), (-1,1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) == king:
                        print("Success")
                        return

            # Bishop
            elif piece == "B":
                for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                    nr, nc = r, c
                    while 0 <= nr+dr < n and 0 <= nc+dc < n:
                        nr += dr
                        nc += dc
                        if board[nr][nc] != ".":
                            if (nr,nc) == king:
                                print("Success")
                                return
                            break

            # Rook
            elif piece == "R":
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r, c
                    while 0 <= nr+dr < n and 0 <= nc+dc < n:
                        nr += dr
                        nc += dc
                        if board[nr][nc] != ".":
                            if (nr,nc) == king:
                                print("Success")
                                return
                            break

            # Queen
            elif piece == "Q":
                for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r, c
                    while 0 <= nr+dr < n and 0 <= nc+dc < n:
                        nr += dr
                        nc += dc
                        if board[nr][nc] != ".":
                            if (nr,nc) == king:
                                print("Success")
                                return
                            break

    print("Fail")