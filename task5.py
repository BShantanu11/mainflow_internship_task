
# Find all permutations of a string

from itertools import permutations

def all_permutations(s):
    return [''.join(p) for p in permutations(s)]

print(all_permutations("abc"))


# nth Fibonacci number using dynamic programming

num1 = int(input("Enter n to find nth fibonacci number : "))
fibArray = [0, 1]
if(num1 < 3) :
    print("The fibonacci term at", num1, "is :", fibArray[num1 - 1])
else :
    num1 -= 2
    t1 = 0
    t2 = 1
    for i in range(num1) :
        t3 = t1 + t2
        fibArray.append(t3)
        t1 = t2
        t2 = t3
    print("The fibonacci term at", num1 + 2, "is :", fibArray[len(fibArray) - 1])


# Find Duplicates in a List

from collections import Counter

def find_duplicates(lst):
    count = Counter(lst)
    return [item for item, freq in count.items() if freq > 1]

print(find_duplicates([1, 2, 3, 2, 4, 5, 1, 6]))


# Longest Increasing Subsequence

def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))


# Find K Largest Elements

import heapq

def k_largest_elements(nums, k):
    return heapq.nlargest(k, nums)

print(k_largest_elements([3, 1, 5, 12, 2, 11], 3))


# Rotate Matrix (90 Degrees Clockwise)

def rotate_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated = rotate_matrix(matrix)
for row in rotated:
    print(row)


# Sudoku Validator

def is_valid_sudoku(board):
    def is_valid_block(block):
        nums = [i for i in block if i != "."]
        return len(nums) == len(set(nums))

    for i in range(9):
        row = board[i]
        column = [board[j][i] for j in range(9)]
        if not is_valid_block(row) or not is_valid_block(column):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            grid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_block(grid):
                return False

    return True

sudoku_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(is_valid_sudoku(sudoku_board))



# Enhanced Virtual Stock Market Simulator

import random
import time

class StockMarketSimulator:
    def __init__(self, initial_balance=10000):
        self.stocks = {
            'AAPL': 150.0,
            'GOOG': 2800.0,
            'TSLA': 700.0,
            'AMZN': 3400.0,
            'MSFT': 300.0
        }
        self.balance = initial_balance
        self.portfolio = {}
        self.transaction_history = []

    def simulate_price_change(self):
        for stock in self.stocks:
            change_percent = random.uniform(-3, 3)
            self.stocks[stock] = round(self.stocks[stock] * (1 + change_percent / 100), 2)

    def display_stocks(self):
        print("\nCurrent Stock Prices:")
        for stock, price in self.stocks.items():
            print(f"{stock}: ${price}")
        print()

    def display_portfolio(self):
        print("\n💼 Your Portfolio:")
        if not self.portfolio:
            print("You don’t own any stocks yet.")
        else:
            for stock, shares in self.portfolio.items():
                print(f"{stock}: {shares} shares @ ${self.stocks[stock]} each")
        print(f"Available Balance: ${self.balance:.2f}\n")

    def buy_stock(self, symbol, shares):
        if symbol not in self.stocks:
            print("Invalid stock symbol.")
            return
        cost = self.stocks[symbol] * shares
        if self.balance >= cost:
            self.balance -= cost
            self.portfolio[symbol] = self.portfolio.get(symbol, 0) + shares
            self.transaction_history.append(f"Bought {shares} shares of {symbol} at ${self.stocks[symbol]}")
            print(f"Bought {shares} shares of {symbol} for ${cost:.2f}")
        else:
            print("Insufficient balance to buy.")

    def sell_stock(self, symbol, shares):
        if symbol not in self.portfolio or self.portfolio[symbol] < shares:
            print("Not enough shares to sell.")
            return
        revenue = self.stocks[symbol] * shares
        self.portfolio[symbol] -= shares
        if self.portfolio[symbol] == 0:
            del self.portfolio[symbol]
        self.balance += revenue
        self.transaction_history.append(f"Sold {shares} shares of {symbol} at ${self.stocks[symbol]}")
        print(f"Sold {shares} shares of {symbol} for ${revenue:.2f}")

    def show_transaction_history(self):
        print("\nTransaction History:")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for tx in self.transaction_history:
                print("-", tx)
        print()

    def run(self) :
        while True :
            self.simulate_price_change()
            print("\n==== Virtual Stock Market Simulator ====")
            print("1. View Stock Prices")
            print("2. View Portfolio")
            print("3. Buy Stocks")
            print("4. Sell Stocks")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Enter your choice : ")

            if choice == "1" :
                self.display_stocks()
            elif choice == "2" :
                self.display_portfolio()
            elif choice == "3" :
                self.display_stocks()
                symbol = input("Enter stock symbol to buy: ").upper()
                try :
                    shares = int(input("Enter number of shares to buy: "))
                    self.buy_stock(symbol, shares)
                except ValueError :
                    print("Invalid input for shares.")
            elif choice == "4" :
                symbol = input("Enter stock symbol to sell: ").upper()
                try :
                    shares = int(input("Enter number of shares to sell: "))
                    self.sell_stock(symbol, shares)
                except ValueError :
                    print("Invalid input for shares.")
            elif choice == "5" :
                self.show_transaction_history()
            elif choice == "6" :
                print("Exiting the simulator. Thanks for using it!")
                break
            else :
                print("Invalid choice.")

            time.sleep(1)
