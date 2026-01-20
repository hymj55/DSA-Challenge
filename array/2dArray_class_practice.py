from array import array

board1 = [
    [00, "01", "02"],
    [10, 11, 12],
    [20, 21, 22]
]

print(board1)

print(board1[1][2]) # 12

print(board1[0][1]) # 01

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(board)    #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
board[0][0] = 10
print(board)    #[[10, 2, 3], [4, 5, 6], [7, 8, 9]]

#Rows - ABC, Columns - Seat Number number, Assignment - occupied X, otherwise an 0

cinema = [
    ["1", "A", "X"],
    ["2", "B", "O"],
    ["3", "C", "X"]
]
# cinema is 2D array / matrix
print("2D array")
rows, cols = 3, 3
array_2d = [[0 for _ in range(cols)] for _ in range(rows)]  #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print(array_2d)

cinema[0][0]="5"

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

scores = [
    [90, 85, 78],   #Student 0, scores in Math, Eng, ComputerS
    [88, 92, 80],   #Student 1
    [75, 85, 89]    #Student 2
]

print("Score Matrix")
print(scores)

for row in scores:  #loop through each row
    print(row)

totals = [sum(row) for row in scores]
print("total score per student:", totals)

#How to get the average score overall per student

#Average score per subject
#How many subjects there are -> column sum!!!

subjects = len(scores[0])   # num of subjects
average = [sum(scores[i][j] for i in range (len(scores))) / len(scores) for j in range(subjects)]
print("average score per subject:", average)


transpose = [[scores[i][j] for i in range(len(scores))] for j in range(len(scores[0]))]
print("transpose matrix")
for row in transpose:
    print(row)


max_score = max(max(row) for row in scores)
print("max score:", max_score)

count = sum(1 for row in scores for score in row if score > 85)
print("count:", count)