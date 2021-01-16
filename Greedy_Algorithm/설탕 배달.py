count = int(input())
data_list = [5,3]
def min_bucket_count(count):
    data_list.sort(reverse=True)
    total_bucket_num = 0
    while(count > 0):
        if(count < 5 && count!=3):
            return -1
            break
        elif count % 15 == 0 || count % 5 == 0:
            total_bucket_num = count / 5
            break
        else:
            count-=5
            if(count % 3 == 0)

        

print(min_bucket_count(count))

//반례 16 



# count = int(input())
# data_list = [5,3]
# def min_bucket_count(count):
#     data_list.sort(reverse=True)
#     total_bucket_num = 0
#     for data in data_list:
#         bucket_num = count // data
#         total_bucket_num += bucket_num
#         count -= bucket_num * data
#     if(count>0):
#         return -1

#     else:
#         return total_bucket_num

# print(min_bucket_count(count))

//반례 16 