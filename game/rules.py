import random, copy


def isWinner(grid, draw):
    return ((grid[6].draw == draw and grid[7].draw == draw and grid[8].draw == draw) or 
    (grid[3].draw == draw and grid[4].draw == draw and grid[5].draw == draw) or 
    (grid[0].draw == draw and grid[1].draw == draw and grid[2].draw == draw) or 
    (grid[6].draw == draw and grid[3].draw == draw and grid[0].draw == draw) or 
    (grid[7].draw == draw and grid[4].draw == draw and grid[1].draw == draw) or 
    (grid[8].draw == draw and grid[5].draw == draw and grid[2].draw == draw) or 
    (grid[6].draw == draw and grid[4].draw == draw and grid[2].draw == draw) or 
    (grid[8].draw == draw and grid[4].draw == draw and grid[0].draw == draw)) 


def isGridFull(grid):
    blankSpaces = 9
    for rect in grid:
        if rect.draw != '':
            blankSpaces -= 1
    
    if blankSpaces == 0:
        return True
    else:
        return False


def computerMove(grid):
    possibleMoves = [x for x, rect in enumerate(grid) if rect.draw == '']
    move = -1

    for draw in ['O', 'X']:
        for i in possibleMoves:
            gridCopy = copy.deepcopy(grid)

            gridCopy[i].draw = draw

            if isWinner(gridCopy, draw):
                for r in grid: print(r.draw)
                move = i
                return move
    
    cornersOpen = []
    for i in possibleMoves:
        if i in [0,2,6,8]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [1,3,5,7]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

    return move


def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]
