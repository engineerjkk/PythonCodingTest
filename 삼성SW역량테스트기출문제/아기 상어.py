
# 필요한 모듈 및 라이브러리 import
from collections import deque  # deque 모듈을 가져옵니다.
import sys  # sys 모듈을 가져옵니다.
input = sys.stdin.readline  # input 함수를 표준 입력에서 읽어옵니다.

# 입력값 받기
n=int(input())  # 정수 하나를 입력받아 n에 할당합니다.
sea=[]  # 빈 리스트를 생성합니다.
for i in range(n):  # n번 반복합니다.
    tmp=list(map(int,input().split()))  # 공백을 기준으로 나뉘어진 입력값을 리스트로 변환하여 tmp에 할당합니다.
    sea.append(tmp)  # tmp를 sea 리스트에 추가합니다.
shark_size=2  # 상어 크기를 2로 초기화합니다.
dx=[-1,0,1,0]  # 상, 우, 하, 좌 방향으로의 이동을 위한 리스트를 생성합니다.
dy=[0,1,0,-1]

# BFS 함수 정의
def bfs(x,y,shark_size):
    visited=[[False]*n for _ in range(n)]  # n x n 크기의 2차원 리스트를 False로 초기화합니다.
    distance=[[False]*n for _ in range(n)]  # n x n 크기의 2차원 리스트를 False로 초기화합니다.
    eats=[]  # 빈 리스트를 생성합니다.

    q=deque()  # 빈 deque 객체를 생성합니다.
    q.append((x,y))  # 초기 상어의 위치를 큐에 추가합니다.
    visited[x][y]=True  # 상어의 위치를 방문했음을 표시합니다.

    while q:  # 큐가 빌 때까지 반복합니다.
        x, y = q.popleft()  # 큐에서 좌표를 하나 꺼냅니다.
        for i in range(4):  # 상, 우, 하, 좌 방향에 대해 반복합니다.
            nx = x+dx[i]  # 다음 x 좌표를 계산합니다.
            ny = y+dy[i]  # 다음 y 좌표를 계산합니다.

            if 0<=nx<n and 0 <=ny<n and not visited[nx][ny]:  # 범위 내에 있고 방문하지 않았다면
                if sea[nx][ny] <=shark_size:  # 상어가 지나갈 수 있는 경우
                    q.append((nx,ny))  # 큐에 좌표를 추가합니다.
                    visited[nx][ny] = True  # 해당 위치를 방문했음을 표시합니다.
                    distance[nx][ny]=distance[x][y]+1
                    if sea[nx][ny] < shark_size and sea[nx][ny] !=0:  # 먹을 수 있는 물고기인 경우
                        eats.append((nx,ny,distance[nx][ny]))  # 먹을 수 있는 물고기의 위치와 거리를 추가합니다.
    return sorted(eats, key=lambda x:((x[2],x[0],x[1])))  # 먹을 수 있는 물고기를 거리, x좌표, y좌표 순으로 정렬하여 반환합니다.

# 초기화
time=0  # 시간을 초기화합니다.
eat_cnt=0  # 먹은 물고기 수를 초기화합니다.

# 상어의 초기 위치 찾기
for i in range(n):  # n번 반복합니다.
    for j in range(n):  # n번 반복합니다.
        if sea[i][j]==9:  # 상어의 위치를 찾습니다.
            x,y=i,j  # 상어의 위치를 x, y에 할당합니다.

# 이동 및 먹이 찾기
while True:  # 무한 루프를 시작합니다.
    shark = bfs(x,y, shark_size)  # BFS를 통해 먹을 수 있는 물고기를 찾습니다.
    if not shark:  # 먹을 수 있는 물고기가 없다면 
        break  # 반복문을 종료합니다.
    nx, ny, d = shark[0]  # 가장 가까운 물고기의 위치와 거리를 가져옵니다.
    time +=d  # 시간을 더합니다.
    eat_cnt +=1  # 먹은 물고기 수를 증가시킵니다.

    if shark_size ==eat_cnt:  # 상어의 크기와 먹은 물고기 수가 같다면
        shark_size +=1  # 상어의 크기를 증가시킵니다.
        eat_cnt =0  # 먹은 물고기 수를 초기화합니다.

    sea[x][y]=0  # 상어가 이동했으니, 그 위치는 비워둡니다.
    x,y = nx, ny  # 상어의 위치를 업데이트합니다.

print(time)  # 결과 시간을 출력합니다.

#1. n입력받기
#2. sea 만들기
#3. bfs 함수 만들기
#3 1. visited와 distance 초기화하고 queue 만들고 while문 생성
#3 2. queue에서 하나씩 빼서 주변체크해서 shark보다 작거나 같으면 queue,방문,거리 체크
#3 3. shark보다 작으면서 방문했으면 좌표와 거리를 eats에 넣기
#3 4. 정렬해서 리턴
#4. time,eat_cnt 초기화 후 shark 좌표 찾고
#5. while True해서 bfs로 찾고, shark가 없을때까지 그리고 time과 eat_cnt증가
#6. 만약 shark_size와 eat_cnt가 같으면 크기 증가 후 초기화
#7. shark가 이동했으니 기존자리 0 초기화, 그리고 현재 shark 위치 초기화