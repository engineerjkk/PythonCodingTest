from itertools import combinations
import copy
from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]  # down, up, right, left
dc = [0, 0, 1, -1]


def check(board):
    que = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                que.append((i, j))
    while que:
        r, c = que.popleft()
        for d in range(4):
            y = r + dr[d]
            x = c + dc[d]
            if -1 < x < m and -1 < y < n and board[y][x] == 0:
                board[y][x] = 2
                que.append((y, x))

    result = 0
    for i in range(len(board)):
        result += board[i].count(0)
    return result


n, m = map(int, input().split())
board = []
blank = []
result = 0

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 0:
            blank.append((i, j))
    board.append(temp)

nCr = combinations(blank, 3)
print(nCr)
for x in nCr:
    print(x)
    print("----")
    tempBoard = copy.deepcopy(board)
    for i, j in x:  # 선택된 벽 3개 위치
        tempBoard[i][j] = 1
    result = max(result, check(tempBoard))

print(result)
