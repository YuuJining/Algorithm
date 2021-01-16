people = int(input())
time = map(int, input().split())
time_list = list(time)
time_list.sort()

def min_money_time(people):
    total_money_time = 0
    i = 0
    for data in time_list:
        total_money_time += data * (people-i)
        i += 1
    return total_money_time

print(min_money_time(people))