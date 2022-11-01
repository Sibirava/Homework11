def enter_elements_row():
    ls = []

    element = 0

    while element != -1:
        element = int(input("Input element in a row:"))
        if element == -1:
            break
        else:
            ls.append(element)
    return ls

def check_palindrome(ls):

    if len(ls) % 2 == 0:
        central_element = round(len(ls) / 2)
        ls1 = ls[:central_element]
        new_ls = ls[central_element:]
        new_ls = new_ls[::-1]
        if ls1 == new_ls:
            return True
    return False

def main():
    ls = enter_elements_row()

    if check_palindrome(ls):
        msg = f"Elements are mirrored to the middle of the list{ls}"
    else:
        msg = f"Elements of list {ls} are not mirrored"

    print(msg)
main()

