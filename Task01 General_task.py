def enter_elements_row(number_vector_elements):
    ls = [int(input("Input element of list:")) for i in range(number_vector_elements)]
    return ls

def get_max_element(ls):
    max = ls[0]

    for element in ls:
        if element > max:
            max = element
    return max

def get_min_element(ls):
    min = ls[0]

    for element in ls:
        if element < min:
            min = element
    return min

def find_avg(ls):
    sum = 0

    for element in ls:
        sum += element
    return round(sum / len(ls), 2)

def count_element(ls):
    count_negative = 0
    count_zero = 0
    count_positive = 0

    for element in ls:
        if element < 0:
            count_negative += 1
        elif element == 0:
            count_zero += 1
        else:
            count_positive += 1
    return(count_negative, count_zero, count_positive)

def get_first_max_value_index(ls):
    max_index = 0

    for index in range(len(ls)-1, -1, -1):
        if ls[index] >= ls[max_index]:
            max_index = index
    return max_index

def get_first_min_value_index(ls):
    min_index = 0

    for index in range(len(ls)-1, -1, -1):
        if ls[index] <= ls[min_index]:
            min_index = index
    return min_index

def change_min_max_value(ls):

    max_index = get_first_max_value_index(ls)
    min_index = get_first_min_value_index(ls)
    change_index = ls[max_index]

    for index in range(0, 1, len(ls) + 1):
        ls[max_index] = ls[min_index]
        ls[min_index] = change_index
    return ls


def main():

    number_vector_elements = int(input(f"Input number of list elements: "))
    ls = enter_elements_row(number_vector_elements)

    negative, zero, positive = count_element(ls)

    msg = (f"{ls} \n"
           f"1)Max value in ls is {get_max_element(ls)}. Index of first max value is "
           f"{get_first_max_value_index(ls)}. \n"
           f"2)Min value is {get_min_element(ls)} Index of first min value is "
           f"{get_first_min_value_index(ls)} \n "
           f"3)The avg of a row is {find_avg(ls)} \n "
           f"4) Count of negative numbers in ls is {negative}, count of zeros is {zero},\n"
           f"count of positive numbers is {positive}.\n"
           f"5)If we swap places of max and min values we'll get new list "
           f"{change_min_max_value(ls)}")
    print(msg)

main()