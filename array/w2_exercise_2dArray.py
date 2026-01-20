# Exercise 1 - Treasure Sweep (“snake” path)
# Your robot janitor must collect coins from a grid room. Traverse the matrix in a snake pattern:
# left→right on row 0, right→left on row 1, left→right on row 2, ...
# Return the visit order as a 1D list and the total coins collected.
# Steps:
# 1. Loop over rows; reverse odd-indexed rows before adding.
# 2. Keep a running sum.
# Examples:
# Input: grid = [[5,1,3],[2,0,4],[7,6,8]]
# Output order: [5,1,3,4,0,2,7,6,8]
# Total: 36
from operator import index

print("Exercise 1")
grid = [
    [5,1,3],
    [2,0,4],
    [7,6,8]
]

final_1d_array = []
current_col = 0
total_coin = 0

for i in range (len(grid)): #3   0,1,2
    if i % 2 == 0:
        for j in range(len(grid[i])): #3   0,1,2
            final_1d_array.append(grid[i][j])
            total_coin += grid[i][j]
            current_col = j
    else:
        for j in range(len(grid[i])):
            final_1d_array.append(grid[i][current_col])
            total_coin += grid[i][current_col]
            current_col -= 1

print("Final 1D Array: ", final_1d_array)
print("Total: ", total_coin)



# Exercise 2 - “Flip the Scoreboard” (Transpose Matrix)
# A digital scoreboard was mounted sideways. Transpose the matrix (rows ↔ columns) without using libraries.
# Steps:
# 1. If matrix is m x n, create n x m result.
# 2. Copy result[c][r] = matrix[r][c].
# Examples:
# Input: board = [[1,2,3],[4,5,6]] (2×3)
# Output: [[1,4],[2,5],[3,6]] (3×2)
print("\nExercise 2")
board = [
    [1,2,3],
    [4,5,6]
] # 2*3

rows = len(board)   #2
cols = len(board[0]) #3
transposed = []

for i in range(cols): #3  i = 0,1,2
    new_row = []
    for j in range(rows): #2  j=0,1
        new_row.append(board[j][i])
    transposed.append(new_row)
print("transposed: ", transposed)

#Second Way: List comprehension
transposed_lc = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]
print("transposed_lc: ", transposed_lc)

#Declaring 2D array
# array_2d = [[0 for _ in range(cols)] for _ in range(rows)]

# Exercise 3 - Pixel Strip (Flatten Matrix → 1D)
# You need to stream pixel rows to a tiny LED strip. Flatten a 2D matrix into a row-major 1D list.
# Steps:
# 1. Visit rows top→bottom.
# 2. Within each row, visit left→right and append to a single list.
# Examples:
# Input: pixels = [[9,8],[7,6],[5,4]]
# Output: [9,8,7,6,5,4]
print("\nExercise 3")
pixels = [
    [9,8],
    [7,6],
    [5,4]
]
flattened = []

for i in range(len(pixels)): #3 i=0,1,2
    for j in range(len(pixels[i])): #2  j=0,1
        flattened.append(pixels[i][j])

print("Flattened: ", flattened)

flat = []

for row in pixels:
    for x in row:
        flat.append(x)

print("\neasy: ", flat)


flat = [x for row in pixels for x in row]


# Exercise 4 - Max Row/Column Sum
# In a cafeteria grid, each cell has the number of snacks sold. Find the row with the highest total and
# the column with the highest total. If there’s a tie, pick the smallest index.
# Steps:
# 1. Compute all row sums; take argmax with tie-break.
# 2. Compute all column sums; take argmax with tie-break.
# 3. Return (best_row_index, best_row_sum, best_col_index, best_col_sum).
# Examples:
# Input: sales = [[3, 1, 4], [2, 9, 5], [8, 2, 6]]
# Row sums = [8, 16, 16] → best row index = 1 (tie goes to smaller index), sum 16
# Col sums = [13, 12, 15] → best col index = 2, sum 15
# Output: (1, 16, 2, 15)
print("\nExercise 4")
sales = [
    [3, 1, 4],
    [2, 9, 5],
    [8, 2, 6]
]

# for row in sales:
#     print(row)

row_sums = [sum(row) for row in sales] #[8, 16, 16]
print("Row sums = ", row_sums)
best_row = max(row_sums)
print("best_row", best_row)

best_row_index = row_sums.index(best_row)
print("best_row_index: ", best_row_index)
# best_row_index_l = row_sums.index(best_row, 2)
# print("best_row_index_l: ", best_row_index_l)

num_col = len(sales[0]) #3
col_sums = []

for i in range(num_col): #3  i=0,1,2
    sums = 0
    for j in range(len(sales)): #3  j=0,1,2
        sums += sales[j][i]
    col_sums.append(sums)
print("Col sums = ", col_sums)  # [13, 12, 15]

# #Second Way: List comprehension for column sums
# col_sums_lc = [sum(sales[j][i] for j in range(len(sales))) for i in range(num_col)]
# print("Col_sums_lc = ", col_sums_lc)

best_col = max(col_sums)
print("best_col:", best_col)

best_col_index = col_sums.index(best_col)
print("best_col_index: ", best_col_index)

final = [best_row_index, best_row, best_col_index, best_col]
print(tuple(final))

# Exercise 5 - "Diagonal Delivery" (Sum of Diagonals)
# A delivery drone must drop packages along both diagonals of a square city grid. Given an n x n
# matrix, return the sum of the main diagonal (top-left → bottom-right) and the sum of the anti-
# diagonal (top-right → bottom-left). If n is odd, do not double-count the center element.
# Steps:
# 1. Loop through each row i.
# 2. Add matrix[i][i] to the main diagonal sum.
# 3. Add matrix[i][n - 1 - i] to the anti-diagonal sum.
# 4. If n is odd, subtract the center once from the total.
# Examples:
# Input: grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Main diagonal sum = 1 + 5 + 9 = 15
# Anti-diagonal sum = 3 + 5 + 7 = 15
# Total (without double-count) = 25
# Output: (15, 15, 25)
print("\nExercise 5")
def diagonal_sum(matrix):
    n = len(matrix)
    main_sum = 0
    anti_sum = 0
    for i in range(n):
        main_sum += matrix[i][i]
        anti_sum += matrix[i][n-1-i]
    total = main_sum + anti_sum
    if n % 2 == 1:
        total = total - matrix[n // 2][n // 2]
    return main_sum, anti_sum, total

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = diagonal_sum(grid)
print(result)
print("test")
main, anti, total = diagonal_sum(grid)
print(main, anti, total)


print("\n test")
mat = [[7 for _ in range(3)] for _ in range(3)]
print(mat)

for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j], end=" ")

print("\n")
rows, cols = 4, 3
td = [[0 for _ in range(cols)] for _ in range(rows)]
print(td)