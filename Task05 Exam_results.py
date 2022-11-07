def enter_exam_marks(number_students):

    marks = [int(input("Input element of list:")) for i in range(number_students)]
    return marks

def calc_exam_results(mark, marks):
    count = 0
    for i in range(len(marks)):
        if mark == marks[i]:
            count += 1
        if not 0 <= marks[i] <= 5:
            return -1
    return count

def main():
    number_students = int(input("Input number od students: "))
    marks = enter_exam_marks(number_students)

    name_marks = ["zeros", "units", "deuces", "triplets", "fours", "fives"]

    for i in range(len(name_marks)):
        result = calc_exam_results(i, marks)
        if result == -1:
            print(f"Please enter valid marks (from 0 to 5).")
            break
        msg = f"{name_marks[i]} - {round(result * 100 / len(marks), 2)}% - ({result})"
        print(msg)
main()

