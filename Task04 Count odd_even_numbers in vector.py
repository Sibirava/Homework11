import random

def random_vector_elements():
   n = 10
   vector = [random.randrange(100) for i in range(n)]
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