from collections import deque
import sys
input = sys.stdin.readline

n=int(input())
sea=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    sea.append(tmp)

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(x,y,shark_size):
    visited=[[False]*n for _ in range(n)]
    distance=[[False]*n for _ in range(n)]
    visited[x][y]=True
    eats=[]
    q=deque()
    q.append((x,y))
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if -1<nx<n and -1<ny<n and not visited[nx][ny]:
                if sea[nx][ny]<=shark_size:
                    q.append((nx,ny))
                    visited[nx][ny]=True
                    distance[nx][ny]=distance[x][y]+1
                    if sea[nx][ny]<shark_size and sea[nx][ny] != 0:
                        eats.append((nx,ny,distance[nx][ny]))
    return sorted(eats,key=lambda x:((x[2],x[0],x[1])))
time=0
eat_cnt=0
for i in range(n):
    for j in range(n):
        if sea[i][j]==9:
            x,y = i,j
shark_size=2

while True:
    shark=bfs(x,y,shark_size)
    if not shark:
        break
    nx,ny,d=shark[0]
    time+=d
    eat_cnt+=1
    if shark_size==eat_cnt:
        shark_size+=1
        eat_cnt=0
    sea[x][y]=0
    x,y=nx,ny
print(time)