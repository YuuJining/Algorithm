count = int(input())
money_list=[500,100,50,10,5,1]
def min_money_count(count):
    real_count = 1000 - count
    count_total = 0
    for data in money_list:
        money_count = real_count // data
        real_count -= money_count * data
        count_total += money_count
    return count_total
print(min_money_count(count))        