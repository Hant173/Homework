#Bài 1 Đếm số
#my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
#Trả ra
#{10: 1, 21: 2, 40: 3, 52: 2, 1: 2, 2: 4, 11: 4, 25: 1, 24: 2, 60: 1}

print('Ta có list: [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]')
my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
count = 0
Dict = {}
for a in my_list: 
    for b in my_list:
        if a == b:
            count = count +1
    Dict[a] = count
    count = 0
print('Từ điển là:', Dict)

#Bài 2
#Viết chương trình in ra thời gian đếm ngược đến XMas 2021 sau mỗi khoảng thời gian nhất định.
#vd in ra sau mỗi 5s:
#Countdown to Xmas 2021: 112 days, 11:47:01.339588
#Countdown to Xmas 2021: 112 days, 11:46:56.324008
#Countdown to Xmas 2021: 112 days, 11:46:51.310473

import datetime
import time
datetime_XMas = datetime.datetime(2021, 12, 24, 00, 00, 00, 000000)
while True:
    datetime_now = datetime.datetime.now()
    time_countdown = datetime_XMas - datetime_now
    print('Countdown to Xmas 2021: ',time_countdown)
    time.sleep(5)
    if datetime_now >=datetime_XMas:
        break

# Bài 3 
#Cho một list gồm 1 hoặc nhiều từ điển (Dictionary). Viết chương trình để trả ra tập hợp tất cả các giá trị (values) duy nhất trong tất cả danh sách các từ điển trên.
#[VD1]: Trường hợp dưới đây danh sách đầu vào có 1 từ điển map tên người vào tuổi của họ. Trả ra set các tuổi duy nhất.
#unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]) == {22, 25, 26, 27, 38}
#[VD2]: Trường hợp dưới đây danh sách đầu vào có 7 dicts, mỗi dict chỉ có 1 cặp key-values. 5 giá trị trả về là duy nhất.

my_list=[dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]
s = set(val for dic in my_list for val in dic.values())
print(s)

# Bài 4
#Cho list A chứa các số nguyên đã sắp xếp theo thứ tự tăng dần.
#Vd A = [3, 6, 7, 9, 11, 12] và một số nguyên sum. Tìm tất cả các cặp số (a,b) trong mảng A có tổng bằng sum
#vd ở đây nếu sum = 18 thì kết quả là [(7,11), (6,12)]. Nếu không có cặp số nào thỏa mãn thì in ra list rỗng []
#unique_value_dict([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]) == {'S009', 'S007', 'S002', 'S001', 'S005'}

print('Mời bạn nhập một số sum bất kỳ: ') 
number_sum = int(input())
list=[]
j_index_my_list = 1
my_list = [3, 6, 7, 9, 11, 12]
for a in my_list:
    for b in range(j_index_my_list,len(my_list)):
        if a + my_list[b] == number_sum:
            _tuple = (a,my_list[b])
            list.append(_tuple)
            break
    j_index_my_list +=1
print(list)

