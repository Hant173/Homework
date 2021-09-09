#Bài 1
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

