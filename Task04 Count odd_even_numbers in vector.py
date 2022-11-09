import random

RANDOM_VALUE_DOWN = -100
RANDOM_VALUE_UP = 100
NUMBER_VECTOR_ELEMENTS = 10
def random_vector_elements():

   vector = [random.randint(RANDOM_VALUE_DOWN, RANDOM_VALUE_UP) for i in range(NUMBER_VECTOR_ELEMENTS)]
   return vector

def count_odd_elements(vector):
    odd_number = 0

    for i in vector:
        if i % 2 == 1:
            odd_number += 1
    return odd_number

def count_even_elements(vector):
    even_number = 0

    for i in vector:
        if i % 2 == 0:
            even_number += 1
    return even_number


def main():
    vector = random_vector_elements()

    msg = f"In vector{vector} there are {count_even_elements(vector)} even numbers and \n" \
          f"{count_odd_elements(vector)} odd numbers."
    print(msg)

main()