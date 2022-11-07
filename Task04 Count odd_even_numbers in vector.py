import random

RANDOM_VALUE_DOWN = -100
RANDOM_VALUE_UP = 100
NUMBER_VECTOR_ELEMENTS = 10
def random_vector_elements():

   vector = [random.randint(RANDOM_VALUE_DOWN, RANDOM_VALUE_UP) for i in range(NUMBER_VECTOR_ELEMENTS)]
   return vector

def count_odd_even_elements(vector):
    even_number = 0
    odd_number = 0

    for i in vector:
        if i % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
    return(even_number, odd_number)


def main():
    vector = random_vector_elements()

    even_number, odd_number = count_odd_even_elements(vector)
    msg = f"In vector{vector} there are {even_number} even numbers and \n" \
          f"{odd_number} odd numbers."
    print(msg)

main()