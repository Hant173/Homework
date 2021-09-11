#Bai 1
#Viết hàm có đầu vào là 1 chuỗi, trả ra số chữ cái, số ký tự viết hoa, số ký tự viết thường và số chữ số trong chuỗi đó. Giả sử đầu vào sau được cấp cho hàm:
#s = "Hello World! 123"
#Hàm count_char_type(s) sẽ trả ra 1 dict {"LETTERS":10, "CASE": {"UPPER CASE":2, "LOWER CASE":8}, "DIGITS":3}. Lưu ý: value của key "CASE" là một dict có 2 keys là "UPPER CASE", "LOWER CASE".
#a) Viết hàm trên dùng bất kỳ hàm built in nào của python
#b) Viết hàm chỉ dùng 1 hàm built in duy nhất.

def Count(input_str) -> dict:
    upper, lower, number, letter = 0, 0, 0, 0
    for i in range(len(input_str)):
        # LETTER
        if input_str[i].isalpha():
            letter += 1

        if input_str[i].isupper():
            upper += 1
        elif input_str[i].islower():
            lower += 1
        elif input_str[i].isdigit():
            number += 1
    return {
        "LETTERS": letter,
        "CASE": {
            "UPPER CASE": upper,
            "LOWER CASE": lower
        },
        "DIGITS": number
    }
str1 = "Hello World! 123"
print(Count(str1))

#Bài 2
#Cho một list A các điểm thi (từ 0-10) của các học viên trong lớp. Viết 3 hàm tính:
# 1. giá trị trung bình (mean) của dãy.
# 2. trung vị (median) của dãy A. trung vị là một số đứng ở vị trí giữa trong dãy số đã được sắp xếp theo thứ tự tăng dần, median chia dãy số cho trước thành 2 nửa bằng nhau. Nếu độ dài của dãy số là số lẻ, thì số ở giữa là median, nếu chiều dài của dãy số là số chẵn thì median được xác định bằng cách lấy trung bình của hai số ở giữa.
# 3. mode của dãy A. Mode là phần tử có số lần xuất hiện nhiều nhất trong dãy. Mode sẽ giúp ta trả lời câu hỏi: "Trong lớp này, học viên đạt Điểm số nào nhiều nhất?".

def average(data):
    return sum(data) / len(data)

def median(data):
    # sort list
    data.sort()
    # half index
    half = len(data) // 2
    if not len(data) % 2:
        return (data[half - 1] + data[half]) / 2.0
    return data[half]


def most_frequent(data):
    counter = 0

    # find max counter
    for i in data:
        curr_frequency = data.count(i)
        if curr_frequency > counter:
            counter = curr_frequency

    # append results
    results = []
    for i in data:
        curr_frequency = data.count(i)
        if curr_frequency == counter and i not in results:
            results.append(i)

    return results


def my_function(data):
    return average(data), median(data), most_frequent(data)

lst = [15, 9, 55, 41, 35, 20, 62, 49, 15, 9]
print(my_function(lst))