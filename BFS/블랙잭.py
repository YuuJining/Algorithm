N, M = map(int, input().split())
data = [int(i) for i in input().split()]
arr=[]

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if data[i] + data[j] + data[k] <= M:
                arr.append(data[i]+data[j]+data[k])
print(max(arr))               