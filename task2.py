import math

# If number is prime or not
num1 = int(input("Enter a number to check if prime or not : "))
num2 = math.floor(math.sqrt(num1))
i1 = 2
flag = 0
while(i1 <= num2) :
    if(num1 % i1 == 0) :
        print("The number is NOT prime.")
        flag = 1
    i1 += 1
if(num1 == 1) :
    print("The number is neither prime nor composite.")
elif(flag != 1) :
    print("The number is prime.")


# Sum of digits of a number
num3 = int(input("Enter a number to find sum of digits : "))
answer = 0
while(num3 != 0) :
    answer += (num3 % 10)
    num3 = math.floor(num3 / 10)
print("The sum of digits is ", answer)


# Find LCM and GCD
num4 = int(input("Enter first number to find GCD and LCM : "))
num5 = int(input("Enter second number : "))
gcd1 = math.gcd(num4, num5)
lcm1 = math.floor((num4 * num5) / gcd1)
print("GCD of numbers is ", gcd1)
print("LCM of numbers is ", lcm1)


# Reverse the list of integers
list1 = [12, 45, 7, 89, 23, 56, 34, 90, 11, 3]
list2 = []
for i in range(len(list1) - 1, -1, -1):
    list2.append(list1[i])
print("Original List is : ", list1)
print("Reversed List is : ", list2)


# Sort the list using bubble sort
list3 = [12, 45, 7, 89, 23, 56, 34, 90, 11, 3]
print("Original List is : ", list1)
length1 = len(list3)
for i in range(length1 - 1) :
    for j in range(length1 - 1 - i) :
        if(list3[j] > list3[j + 1]) :
            temp = list3[j]
            list3[j] = list3[j + 1]
            list3[j + 1] = temp
print("The sorted list is : ", list3)


# Remove duplicates from the list
list5 = [1, 2, 2, 7, 89, 9, 76, 76, 76, 5, 43, 72, 1, 2]
list4 = []
for i in list5 :
    exists = False
    for j in list4 :
        if(j == i) :
            exists = True
            break
    if(not exists) :
        list4.append(i)
print("The original list is : ", list5)
print("The unique list is : ", list4)


# String length
str1 = input("Enter a string : ")
length2 = 0
for i in str1 :
    length2 += 1
print("The length of the string is : ", length2)


# Number of vowels and consonants in a string 
vowels = 0
consonants = 0
alpha_vowels = "aeiouAEIOU"
for i in str1 :
    if(i.isalpha()) :
        if i in alpha_vowels :
            vowels += 1
        else :
            consonants += 1
print("The number of vowels is : ")
print("The number of consonants is : ")




# Maze Generator

import random
import sys
sys.setrecursionlimit(10000)  # Increase recursion limit for large mazes

# Maze dimensions (must be odd)
ROWS, COLS = 21, 21

# Direction vectors (up, down, left, right)
DIRS = [(-2, 0), (2, 0), (0, -2), (0, 2)]

# Initialize grid with walls
maze = [['#' for _ in range(COLS)] for _ in range(ROWS)]

# Maze generator using DFS
def generate_maze(r, c):
    maze[r][c] = ' '
    directions = DIRS[:]
    random.shuffle(directions)
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 1 <= nr < ROWS - 1 and 1 <= nc < COLS - 1 and maze[nr][nc] == '#':
            maze[r + dr // 2][c + dc // 2] = ' '
            generate_maze(nr, nc)

# Maze solver using DFS (backtracking)
def solve_maze(r, c, end_r, end_c):
    if r == end_r and c == end_c:
        return True

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and maze[nr][nc] in (' ', 'E'):
            if maze[nr][nc] != 'E':
                maze[nr][nc] = '.'  # Mark as part of path
            if solve_maze(nr, nc, end_r, end_c):
                return True
            if maze[nr][nc] != 'E':
                maze[nr][nc] = ' '  # Unmark if dead end

    return False

# Step 1: Generate Maze
generate_maze(1, 1)

# Step 2: Mark Start and End
start = (1, 1)
end = (ROWS - 2, COLS - 2)
maze[start[0]][start[1]] = 'S'
maze[end[0]][end[1]] = 'E'

# Step 3: Solve Maze using DFS
solve_maze(start[0], start[1], end[0], end[1])

# Step 4: Print Maze
for row in maze:
    print(''.join(row))

