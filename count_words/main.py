import sys


def get_words(filename):
    count_data = dict()
    with open(filename, 'r') as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                if word.isalnum():
                    word = word.lower()
                    if word in count_data:
                        count_data[word] += 1
                    else:
                        count_data[word] = 1
    words = list()
    for k, v in count_data.items():
        words.append((k, v))
    return words


def sort_top_func(e):
    return e[1]


def get_top_words(filename):
    words = get_words(filename)
    words.sort(key=sort_top_func, reverse=True)
    return words[0:5]


# This basic command line argument parsing code is provided and
# calls the get_words() and get_top_words() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        words = get_words(filename)
        print(words)
    elif option == '--topcount':
        words = get_top_words(filename)
        print(words)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()

# python main.py --count small.txt
# python main.py --topcount small.txt
