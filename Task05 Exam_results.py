MARK1 = 1
MARK2 = 2
MARK3 = 3
MARK4 = 4
MARK5 = 5
MARK6 = 6


def enter_exam_marks():
    marks = []
    mark = 0

    print("Input student's marks.\n for exit input -1\n")
    while mark != -1:
        mark = int(input("Input mark: "))
        marks.append(mark)
    marks.remove(-1)
    return marks

def calc_exam_results(marks):

    fives = round(marks.count(MARK5) * 100 / len(marks), 1)
    fours = round(marks.count(MARK4) * 100 / len(marks), 1)
    threes = round(marks.count(MARK3) * 100 / len(marks), 1)
    twos = round(marks.count(MARK2) * 100 / len(marks), 1)
    ones = round(marks.count(MARK1) * 100 / len(marks), 1)
    zeros = round(marks.count(MARK6) * 100 / len(marks), 1)

    return(fives, fours, threes, twos, ones, zeros)

def main():

    marks = enter_exam_marks()

    fives, fours, threes, twos, ones, zeros = calc_exam_results(marks)
    msg = f"In marks list {marks} there are: \n"\
          f"fives = {fives}% ({marks.count(5)}) \n"\
          f"fours = {fours}% ({marks.count(4)}) \n"\
          f"trees = {threes}% ({marks.count(3)}) \n"\
          f"twos = {twos}% ({marks.count(2)}) \n"\
          f"ones = {ones}% ({marks.count(1)}) \n"\
          f"zeroes = {zeros}% ({marks.count(0)})"
    print(msg)
main()

