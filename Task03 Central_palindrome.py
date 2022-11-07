def input_vector_element(number_vector_elements):

    vector = [int(input("Input element of list:")) for i in range(number_vector_elements)]
    return vector

def check_palindrome(vector):
    while len(vector) != 0:
        if vector[0] != vector[len(vector) - 1]:
            return False
        vector = vector[1:len(vector) - 1]
    return True


def main():
    number_vector_elements = int(input(f"Input number of list elements: "))
    vector = input_vector_element(number_vector_elements)

    msg = (f"{vector} Vector elements are mirrored." if check_palindrome(vector)
           else f"{vector} Vector elements are not mirrored.")

    print(msg)


main()
