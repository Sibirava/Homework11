def input_vector_element(number_vector_elements):

    vector = [int(input("Input element of list:")) for i in range(number_vector_elements)]
    return vector

def check_vector_elements_UP(vector):

    for i in range(len(vector)-1):
        for j in range(i + 1, len(vector)):
            if vector[i] >= vector[i + 1]:
                return False
    return True

def check_vector_elements_down(vector):

    for i in range(len(vector)-1):
        for j in range(i + 1, len(vector)):
            if vector[i] <= vector[i + 1]:
                return False
    return True

def main():

    number_vector_elements = int(input(f"Input number of list elements: "))
    vector = input_vector_element(number_vector_elements)

    if check_vector_elements_UP(vector):
        msg = f"Elements of vector are UP"
    elif check_vector_elements_down(vector):
        msg = f"Elements of vector are down"
    else:
        msg = "Elements of vector DON'T form ANY sequence"
    print(msg)

main()