from datetime import datetime
# 1
def day_diff(release_date, code_complete_day):
     convert_release_time = datetime.strptime(release_date, "%d/%m/%Y")
     convert_code_complete_day = datetime.strptime(code_complete_day, "%Y-%d-%m")
     number_time = convert_release_time - convert_code_complete_day 
     return number_time.days

# 2 python main.py
def alpha_num(sentence):
    list_words = []
    words = sentence.strip().split()
    for i in words:
        is_text = False
        is_number = False
        for j in i:
            if j.isalpha():
                is_text = True
            elif j.isnumeric():
                is_number= True
            if is_text and is_number:
                list_words.append(i)
                break
    return list_words


                   

