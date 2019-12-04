def check_double_digit(number):
    return len(str(number)) != len(set(str(number)))


def check_double_digit2(i):
    return len(str(i)) != len(set(str(i)))


def calc_possible_passwords():
    count = 0
    for number in range(356777, 777778):
        if not check_double_digit(number):
            continue

        number_string = (str(number))
        for index, digit in enumerate(number_string[:-1]):
            if int(digit) > int(number_string[index+1]):
                break
            if index+1 == len(number_string):
                count += 1

    print(count)


if __name__ == '__main__':
    # Between 356261-846303
    calc_possible_passwords()
