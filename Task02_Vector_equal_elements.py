import random

RANDOM_VALUE_DOWN = -100
RANDOM_VALUE_UP = 100
NUMBER_VECTOR_ELEMENTS = 20
def random_vector_elements():

   vector = [random.randint(RANDOM_VALUE_DOWN, RANDOM_VALUE_UP) for i in range(NUMBER_VECTOR_ELEMENTS)]
   return vector


def check_vector_elements_different(vector):

    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            if vector[i] == vector[j]:
                return False
    return True


def main():
    vector = random_vector_elements()

    msg = f"{vector} \n {check_vector_elements_different(vector)}"

    print(msg)

main()
