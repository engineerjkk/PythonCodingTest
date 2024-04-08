import sys  # sys 모듈을 가져옵니다.
input = sys.stdin.readline  # 표준 입력에서 한 줄을 읽어오는 함수를 input으로 사용합니다.

graph = []  # 빈 리스트를 생성합니다. (미로 정보를 저장할 리스트)
dr = [-1, 0, 1, 0]  # 북, 동, 남, 서 방향으로의 이동을 위한 리스트를 생성합니다.
dc = [0, 1, 0, -1]

# 입력값 받기
n, m = map(int, input().split())  # 공백으로 구분된 두 정수를 입력받아 각각 n과 m에 할당합니다.
# 공백으로 구분된 세 정수를 입력받아 각각 r, c, d에 할당합니다. (로봇 청소기의 초기 위치와 방향)
r, c, d = map(int, input().split())
for _ in range(n):  # n번 반복합니다.
    # 한 줄을 입력받아 공백으로 나눈 후, 정수로 변환하여 리스트로 만들고 그 리스트를 graph에 추가합니다.
    graph.append(list(map(int, input().split())))

graph[r][c] = -1  # 로봇 청소기의 초기 위치를 청소 완료된 곳(-1)으로 표시합니다.
count = 1  # 청소한 칸의 개수를 세기 위한 변수를 1로 초기화합니다. (청소한 칸에 처음 위치한 칸도 포함)

# 로봇 청소기가 미로를 탐색하며 청소하는 과정
while graph[r][c] != 1:  # 청소가 끝난 칸이 아니라면 반복합니다.
    temp = False  # 임시 변수를 False로 초기화합니다.
    for _ in range(4):  # 방향을 돌면서 탐색합니다.
        d -= 1  # 현재 방향에서 왼쪽 방향으로 회전합니다.
        if d == -1:  # 음수가 되면 최댓값인 3인 북쪽으로 다시 초기화.
            d = 3
        nr = r + dr[d]  # 이동할 다음 행의 위치를 계산합니다.
        nc = c + dc[d]  # 이동할 다음 열의 위치를 계산합니다.
        if graph[nr][nc] == 0:  # 이동한 칸이 벽이 아니라면
            r = nr  # 로봇 청소기의 위치를 업데이트합니다.
            c = nc
            graph[r][c] = -1  # 이동한 칸을 청소 완료된 곳(-1)으로 표시합니다.
            count += 1  # 청소한 칸의 개수를 1 증가시킵니다.
            temp = True  # 이동할 수 있었음을 표시합니다.
            break  # 이동했으므로 방향 탐색을 중단하고 다음 이동을 진행합니다.
    if not temp:  # 네 방향 모두 청소할 수 없는 경우
        r += dr[d-2]  # 후진할 다음 행의 위치를 계산합니다.
        c += dc[d-2]  # 후진할 다음 열의 위치를 계산합니다.

# 최종적으로 청소한 칸의 개수를 출력합니다.
print(count)

# 1. graph, dr, dc, n,m, r,c,d, count 초기화 할 것
# while문을 통해서 좌표에 1이 없어질때까지 
# - 네 방향 다 돌면서 업데이트하는데, 청소안했으면 좌표 없뎃 후 청소했다고 표시 후 카운트
# - 네 방향 다 안되면, 후진