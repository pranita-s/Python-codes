# TIME - O(R * C)


def updateBoard(board,click):
  ROW, COL = len(board), len(board[0])
  row,col = click
  if board[row][col] = 'M':
    board[row][col] = 'X'
  else:
    board[row][col] = 'B'
    count = 0
    for i in range(-1,2):
      for j in range(-1,2):
        r,c = row +i, col +j
        if 0<=r<ROW and 0<=c<COL:
          if board[r][c] == 'M':
            count+=1
    
    if count:
      board[row][col] = str(count)
    else:
      for i in range(-1,2):
      for j in range(-1,2):
        r,c = row +i, col +j
        if 0<=r<ROW and 0<=c<COL and board[r][c] == 'E':
          updateBoard(board,(r,c))
      
  return board
