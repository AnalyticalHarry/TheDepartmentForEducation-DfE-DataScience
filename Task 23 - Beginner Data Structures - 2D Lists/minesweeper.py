#input 
grid = [
    ['-', '-', '-', '#', '#'],
    ['-', '#', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '#', '#', '-', '-'],
    ['-', '-', '-', '-', '-']]


#Defining function
def minesweeper(grid):
    #length of row and colums
    rows = len(grid)
    cols = len(grid[0])
    result = []
    #creating for loop to iterate through in range of row
    for i in range(rows):
        #storing iterated value to result
        result.append([])
        #creating nested for loop to iterate through in range of cols
        for j in range(cols):
            #comapring string "#" 
            if grid[i][j] == '#':
                result[i].append('#')
            else:
                #declaring inital count is zero
                count = 0
                #Creating nested loop for checking Neighbours
                for a in range(max(0, i-1), min(i+2, rows)):
                    for b in range(max(0, j-1), min(j+2, cols)):
                        if grid[a][b] == '#':
                            count += 1
                result[i].append(str(count))
    #returning result
    return result

#calling function
minesweeper(grid)