money_count, total_money = map(int, input().split())
def min_money_count(money_count):
    money_detail = list()
    for i in range(1,money_count+1):
        money_detail.append(int(input()))
        money_detail.sort(reverse=True)  
        money_total_count = 0
    for data in money_detail:
        global total_money
        if data < total_money or data == total_money:
            count = total_money // data
            total_money -= count * data
            money_total_count += count
        else:
            continue    
    return money_total_count
print(min_money_count(money_count))      