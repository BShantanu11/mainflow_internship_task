import math

# Table of a number
num1 = int(input("Enter a number to print table : "))
for i in range(1, 11) :
    print(f"{num1} X {i} = {num1 * i}")
print()


# swap two numbers without using third variable
num2 = int(input("Enter a first number : "))
num3 = int(input("Enter a second number : "))
print(f"The value of first number is : {num2} and second number is : {num3}")
num2 = num2 ^ num3
num3 = num2 ^ num3
num2 = num2 ^ num3
print(f"The value of first number is : {num2} and second number is : {num3}")
print()


# If one string is substring of another
str1 = input("Enter a string : ")
str2 = input("Enter another string : ")
if str2 in str1 :
    print("Another string is substring of main string.")
else :
    print("Another string is NOT substring of main string.")
print()


# Decimal to Binary
num4 = int(input("Enter a number to convert to binary : "))
str3 = ""
while(num4 != 0) :
    str3 = str((num4 % 2)) + str3
    num4 //= 2
print("The binary representation is : ", str3)
print()


# Matrix Addition
mat1 = [[1, 2, 3], [4, 5, 6]]
mat2 = [[6, 5, 4], [3, 2, 1]]
row = len(mat1)
col = len(mat1[0])
mat3 = []
for i in range(row) :
    temp = []
    for j in range(col) :
        temp.append(mat1[i][j] + mat2[i][j])
    mat3.append(temp)
print(f"The addition of matrices {mat1} and {mat2} is : {mat3}")
print()


# Matrix Multiplication
mat4 = [[1, 2], [3, 4]]
mat5 = [[5, 6], [7, 8]]
rowA = len(mat4)
colA = len(mat4[0])
colB = len(mat5[0])
mat6 = [[0 for _ in range(colB)] for _ in range(rowA)]

for i in range(rowA) :
    for j in range(colB) :
        for k in range(colA) :
            mat6[i][j] += mat4[i][k] * mat5[k][j]

print(f"The multiplication of matrices {mat4} and {mat5} is : {mat6}")
print()


# Second largest number
list1 = [7, 52, 90, 77, 12, 23, 81, 99]
if(len(list1) < 2) :
    print("No second largest number")
else :
    list1.sort()
    print(f"Second largest number among {list1} is : {list1[-2]}")
print()


# If two strings are anagrams
str4 = input("Enter first string : ")
str5 = input("Enter second string : ")

if(sorted(str4) == sorted(str5)) :
    print("The two strings are Anagrams")
else :
    print("The two strings are NOT Anagrams")
print()


# Tic-Tac-Toe Game
# Initialize board
board = [' ' for _ in range(9)]

def print_board() :
    for row in [board[i*3 : (i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def is_winner(brd, player):
    win_cond = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6]           # diagonals
    ]
    return any(all(brd[i] == player for i in cond) for cond in win_cond)

def is_full(brd):
    return ' ' not in brd

def get_available_moves(brd):
    return [i for i in range(9) if brd[i] == ' ']

def minimax(brd, depth, is_maximizing):
    if is_winner(brd, 'O'):
        return 1
    elif is_winner(brd, 'X'):
        return -1
    elif is_full(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(brd):
            brd[move] = 'O'
            score = minimax(brd, depth + 1, False)
            brd[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(brd):
            brd[move] = 'X'
            score = minimax(brd, depth + 1, True)
            brd[move] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -math.inf
    move = None
    for i in get_available_moves(board):
        board[i] = 'O'
        score = minimax(board, 0, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    return move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, Computer is O.")
    print_board()

    while True:
        # User move
        try:
            user_move = int(input("Enter your move (0-8): "))
            if board[user_move] != ' ':
                print("Spot taken. Try another.")
                continue
        except:
            print("Invalid input. Enter number from 0 to 8.")
            continue
        board[user_move] = 'X'
        print_board()

        if is_winner(board, 'X'):
            print("You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # AI move
        print("Computer is making a move...")
        ai = best_move()
        board[ai] = 'O'
        print_board()

        if is_winner(board, 'O'):
            print("Computer wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

play_game()

