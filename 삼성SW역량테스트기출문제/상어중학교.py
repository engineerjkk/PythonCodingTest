from collections import deque

# 보드의 크기 N과 행동 횟수 M을 입력받음
N, M = map(int, input().split())

# 보드 정보를 입력받음
board = [list(map(int, input().split())) for _ in range(N)]

# 방문 여부를 나타내는 visited 배열 초기화
visited = [[False for _ in range(N)] for _ in range(N)]

# 상하좌우 이동을 위한 dx, dy 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 주어진 위치에서 bfs 탐색을 수행하여 블록의 크기와 무지개 블록의 크기를 반환하는 함수
def bfs(i, j):
    global visited
    rainbow = []  # 무지개 블록을 저장하는 리스트
    q = deque()
    q.append([i, j])
    block_size = 1  # 현재 블록의 크기
    rainbow_size = 0  # 현재 블록과 연결된 무지개 블록의 개수
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = dx[d] + x, dy[d] + y
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    if board[nx][ny] == board[i][j]:  # 같은 색 블록이면
                        q.append([nx, ny])
                        visited[nx][ny] = True
                        block_size += 1

                    elif board[nx][ny] == 0:  # 무지개 블록이면
                        q.append([nx, ny])
                        visited[nx][ny] = True
                        block_size += 1
                        rainbow_size += 1
                        rainbow.append([nx, ny])  # 무지개 블록 추가
    # 무지개 블록의 방문 여부 초기화
    for r in rainbow:
        x, y = r
        visited[x][y] = False
    return block_size, rainbow_size

# 중력 작용 함수
def gravity():
    for i in range(N-2, -1, -1):
        for j in range(N):
            if board[i][j] not in [-2, -1]:
                loc = i + 1
                while loc < N:
                    if board[loc][j] == -2:
                        if board[loc - 1][j] not in [-2, -1]:
                            board[loc][j] = board[loc - 1][j]
                            board[loc - 1][j] = -2
                    loc += 1
    return

# 보드를 시계 방향으로 90도 회전시키는 함수
def rotate():
    global board
    board = [[row[i] for row in board] for i in range(N-1, -1, -1)]
    return

# 주어진 위치의 블록을 제거하고 점수를 반환하는 함수
def delete(i, j):
    color = board[i][j]  # 제거할 블록의 색상 저장
    board[i][j] = -2  # 블록 제거
    q = deque()
    q.append([i, j])
    block_size = 1  # 제거한 블록의 크기
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = dx[d] + x, dy[d] + y
            if 0 <= nx < N and 0 <= ny < N:
                if (board[nx][ny] == color) or (board[nx][ny] == 0):  # 같은 색 또는 무지개 블록이면
                    q.append([nx, ny])
                    board[nx][ny] = -2  # 블록 제거
                    visited[nx][ny] = True  # 무지게 블록 방문처리
                    block_size += 1
    return block_size**2  # 제거한 블록의 크기의 제곱을 반환

# 게임을 푸는 함수
def solve():
    global visited
    score = 0  # 총 점수
    cnt = 0  # 행동 횟수 카운트
    while True:
        cnt += 1
        max_block = 0  # 현재 턴에서 제거한 최대 블록의 크기
        visited = [[False for _ in range(N)] for _ in range(N)]  # 방문 여부 초기화
        candidate = []  # 후보 블록들의 정보를 저장하는 리스트
        # 보드를 탐색하면서 제거 가능한 블록들을 찾음
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and board[i][j] not in [-2, -1, 0]:
                    visited[i][j] = True
                    block_size, rainbow_size = bfs(i, j)
                    if block_size >= 2:
                        candidate.append([block_size, rainbow_size, i, j])
                        max_block = max(max_block, block_size)
        # 더 이상 제거할 수 있는 블록이 없으면 종료
        if max_block < 2:
            break
        # 후보 블록들을 우선순위에 따라 정렬
        candidate.sort(key=lambda x:[-x[0], -x[1], -x[2], -x[3]])
        _, _, i, j = candidate[0]  # 가장 우선순위가 높은 블록 선택
        score += delete(i, j)  # 선택한 블록을 제거하고 점수를 더함
        gravity()  # 중력 작용
        rotate()  # 보드 회전
        gravity()  # 중력 작용
    return score

# 최종적으로 게임을 푸는 함수를 호출하여 결과를 출력
print(solve())
