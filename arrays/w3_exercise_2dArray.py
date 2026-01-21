
rows, cols = 2, 4

array_test = [ [2 for _ in range(cols)] for _ in range(rows)]
print(array_test)


course_marks = [
    [2, 3, 4],
    [6, 7, 8],
    [9, 10, 13]
]

print(f"\n{course_marks}")


print(len(course_marks))

print("Traversing")
for r in range(len(course_marks)):  #len 3, r 변수에는 0/1/2 순차적으로 할당
    for c in range(len(course_marks[0])):   #첫번째 행의 열개수는 3  c 변수에는 0/1/2 할당
        print(course_marks[r][c], end="/")  #00/01/02 이렇게 출력

print("\nTraversing_previous way")
for row in course_marks:
    for col in row:
        print(col, end=" ")

print("\n")
print(course_marks[2][0])

print("\nTransposing")
matrix =[
    [1,2,3],
    [4,5,6]
]

rows = len(matrix) #2   2 rows
cols = len(matrix[0]) #3    3 cols
transposed = []     #2*3 -> row3*col2

for c in range(cols):   #3, 0,1,2
    new_row = []
    for r in range(rows): #2,  0,1
        new_row.append(matrix[r][c])
    transposed.append(new_row)
print(matrix)
print(transposed)

print("\nTransposing-List comprehension")

transposed_lc = [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]
print(transposed_lc)


print("\nSearch_unsorted")
matrix_m = [
    [1, 2, 3],     # Row 0
    [4, 5, 6],     # Row 1
    [7, 8, 9]      # Row 2
]

target = 8
found = False
for i in range(len(matrix_m)):
    for j in range(len(matrix_m[i])):
        if matrix_m[i][j] == target:
            print(f"Found {target} at index of ({i},{j})")
            found = True
            break
        if found:
            break

new_row = [10, 11, 12]
matrix_m.append(new_row)
print(matrix_m)

matrix_m.insert(1, new_row)
print(matrix_m)

del matrix_m[2]
print(matrix_m)

# del matrix_m[0][1]
# print(matrix_m)

print("\ndel")
del_test = [1,2,3]
del del_test[0]
print(del_test)

print("\npop")
pop_test = [1,2,3]
removed = pop_test.pop(0)
print(removed)

print("\nInsert column")
new_col = [100,200,300,400]

for i in range(len(matrix_m)):  #row 0,1,2,3
    matrix_m[i].insert(1, new_col[i]) #m[0].insert(1, new_col[0])
print(matrix_m)

for row in matrix_m:
    print(row)

del matrix_m[1][1]
del matrix_m[3][2]

for row in matrix_m:
    print(row)

print("New")
n_m = [
    [1, 2, 3],     # Row 0
    [4, 5, 6],     # Row 1
    [7, 8, 9]      # Row 2
]


# new_column = [10,20,30]
# for i in range(len(n_m)): #0,1,2
#     n_m.append(new_column[i])
# print(n_m)

# new_column = [10,20,30]
# for i in range(len(n_m)): #0,1,2
#     n_m.insert(3, new_column[i])
# print(n_m)


for row in n_m:
    print(row)

print("Insert New")
n_m2 = [
    [1, 2, 3],     # Row 0
    [4, 5, 6],     # Row 1
    [7, 8, 9]      # Row 2
]

new_column2 = [50,60,70]
for i in range(len(n_m2)): #0,1,2
    n_m2[i].insert(3, new_column2[i])
print(n_m2)

print("del column on n_m2 list")
del_index = 3
for i in range(len(n_m2)):
    del n_m2[i][del_index]
print(n_m2)


row = [12,13,14]
n_m2.append(row.copy())

print("after adding row.copy: ",n_m2)

print("star tree")

star = "*"
for i in range(4):
    if i == 0:
        print(star)
    else:
        print(star * (i+1))


print("star tree2")

rows = 4
for i in range(1, rows+1):
    print("*" * i)


print("star tree-center")
n = 4  # 줄 수
for i in range(n):
    stars = 2 * i + 1   # 홀수 개 별
    spaces = n - i - 1  # 앞쪽 공백
    print(" " * spaces + "*" * stars)


scores = [
    [90, 85, 78],   #Student 0, scores in Math, Eng, ComputerS
    [88, 92, 80],   #Student 1
    [75, 85, 89]    #Student 2
]

print("\nScore Matrix")

for row in scores:  #loop through each row
    print(row)

totals = [sum(row) for row in scores]
print("total score per student:", totals)
