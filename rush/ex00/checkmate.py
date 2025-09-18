#!/usr/bin/env python

def checkmate(board: str):
    rows = board.strip().split("\n")
    n = len(rows)  
    
    if any(len(row) != n for row in rows):
        print("Error")
        return
    
    board = [list(row) for row in rows]

   
    kings = [(r, c) for r in range(n) for c in range(n) if board[r][c] == "K"]

   
    if len(kings) != 1:  
        print("Error")
        return

   
    has_piece = any(cell != '.' for row in board for cell in row)
    if not has_piece:
        print("Error")
        return

    kr, kc = kings[0]
    
    
    for r in range(n):
        for c in range(n):
            piece = board[r][c]
            if piece == "." or piece == "K":
                continue

            # Pawn
            if piece == "P":
                for dr, dc in [(-1,-1), (-1,1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) == (kr,kc):
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
                            if (nr,nc) == (kr,kc):
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
                            if (nr,nc) == (kr,kc):
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
                            if (nr,nc) == (kr,kc):
                                print("Success")
                                return
                            break

    print("Fail")
