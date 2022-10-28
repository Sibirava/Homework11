def enter_elements_row():
    vector = []

    element = 0

    while element != -1:
        element = int(input("Input element in a vector:"))
        if element == -1:
            break
        else:
            vector.append(element)
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

    vector = enter_elements_row()

    if check_vector_elements_UP(vector):
        msg = f"Elements of vector are UP"
    elif check_vector_elements_down(vector):
        msg = f"Elements of vector are down"
    else:
        msg = "Elements of vector DON'T form ANY sequence"

    print(msg)

main()