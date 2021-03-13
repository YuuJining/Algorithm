N = int(input())
positive = []
negative = []
one = []

for _ in range(N):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num <= 0:
        negative.append(num)
    else:
        one.append(num)

positive.sort(reverse=True)
negative.sort()

result = 0

if len(positive) % 2 == 0:
    for i in range(0, len(positive),2):
        result += positive[i] * positive[i+1]
else:
    for i in range(0, len(positive)-1, 2):
        result += positive[i] * positive[i+1]
    result += positive[len(positive)-1]

if len(negative) % 2 == 0:
    for i in range(0. len(negative),2):
        result += negative[i] * negative[i+1]
else:
    for i in range(0, len(nagative)-1, 2):
        result += negative[i] * negative[i+1]
    result += negative[len(negative)-1]        

result += sum(one)
print(result)


// 양수 리스트는 내림차순으로 정렬, 음수 리스트는 오름차순으로 정렬
// 리스트 길이가 짝수면 2개씩 곱해주기
// 리스트 길이가 홀수면 마지막 숫자 빼고 곱해주고 마지막 더하기

// 1은 리스트 따로 만들어서 마지막에 1 더해주기

