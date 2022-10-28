import random
def random_vector_elements():
   n = 10
   vector = [random.randrange(100) for i in range(n)]
   return vector


def check_vector_elements_equal(vector):

    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            if vector[i] == vector[j]:
                return False
    return True


def main():
    vector = random_vector_elements()
    print(vector)

    answer = check_vector_elements_equal(vector)
    print(answer)


main()
