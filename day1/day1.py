import re


def run():
    with open(file="day1/day1_1_input.txt", mode="r") as data:
        # data_raw = data.read()
        calb_nums_list = []
        for line in data:
            line = line.rstrip()
            digit_list = re.findall("\d", line)
            calb_num = ""
            if len(digit_list) > 1:
                calb_num = str(digit_list[0]) + str(digit_list[-1])
            elif len(digit_list) == 1:
                calb_num = str(digit_list[0]) + str(digit_list[0])
            else:
                print("no numbers in input")
            calb_nums_list.append(calb_num)

        total = 0
        for num in calb_nums_list:
            total += int(num)
        print(total)


run()
