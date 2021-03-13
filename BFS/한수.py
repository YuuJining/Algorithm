def Han(n):
    count=0
    if(n<100):
        return n
    else:
        for i in range(100,(n+1)):
            hund = (i//100)
            ten = ((i%100)//10)
            one = ((i%100)%10)

            if((hund - ten) ==(ten-one)):
                count += 1
        return (99+count)

data = int(input())
res = Han(data)
print(res)  

// 99까지는 모두 한수가 성립함
// 100 이후 3자리 수부터는 각 자리 수 비교해 등차수열인지 판단
