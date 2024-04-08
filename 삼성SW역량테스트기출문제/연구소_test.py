from itertools import combinations
from collections import deque
import sys
import copy
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def solution(board):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                queue.append((i, j))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            x = r+dr[i]
            y = c+dc[i]
            if -1 < x < n and -1 < y < m and board[x][y] == 0:
                board[x][y] = 2
                queue.append((x, y))
    result = 0
    for i in range(n):
        result += board[i].count(0)
    return result


board = []
blank = []
result = 0

n, m = map(int, input().split())
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 0:
            blank.append((i, j))
    board.append(tmp)

nCr = combinations(blank, 3)

for x in nCr:
    tmpBoard = copy.deepcopy(board)
    for i, j in x:
        tmpBoard[i][j] = 1
    result = max(result, solution(tmpBoard))

print(result)
