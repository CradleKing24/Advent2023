import re

WORDS_DICT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def insert_num(string, index, num):
    return string[:index] + num + string[index:]


def word_to_num(full_line: str):
    # (?= ) is a lookahead assertion so will capture overlapping words
    word_list = re.findall(
        "(?=(one|two|three|four|five|six|seven|eight|nine))", full_line
    )
    print(full_line)
    line_inserts = {}
    for word in word_list:
        word_index = full_line.index(word)
        if word not in line_inserts:
            loc_list = [word_index]
            line_inserts[word] = loc_list
        else:
            line_inserts[word].append(word_index)
        # full_line = full_line.replace(word, WORDS_DICT[word])
    count = 0
    for word_insert, index_to_insert in line_inserts:
        word_as_num = WORDS_DICT[word_insert]
        for index in index_to_insert:
            pushed_index = int(index) + count
            local_index = full_line.insert(word_insert)
            count += 1

    print(full_line)
    return full_line


def run():
    with open(file="day1/test.txt", mode="r") as data:
        # with open(file="day1/day1_1_input.txt", mode="r") as data:
        # with open(file="day1/puzzle_one_input.txt", mode="r") as data:
        calb_nums_list = []
        for line in data:
            line = line.rstrip()
            line = word_to_num(full_line=line)
            digit_list = re.findall("\d", line)
            # print(digit_list)
            calb_num = ""
            if len(digit_list) > 1:
                calb_num = str(digit_list[0]) + str(digit_list[-1])
            elif len(digit_list) == 1:
                calb_num = str(digit_list[0]) + str(digit_list[0])
            else:
                print("no numbers in input")
            print(calb_num)
            calb_nums_list.append(calb_num)

        total = 0
        # print(calb_nums_list)
        for num in calb_nums_list:
            total += int(num)
        print(total)


run()
