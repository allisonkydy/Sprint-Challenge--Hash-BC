#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for index in range(length):
        diff = limit - weights[index]
        if hash_table_retrieve(ht, diff) is not None:
            a = index
            b = hash_table_retrieve(ht, diff)
            if a > b:
                return (a, b)
            else:
                return (b, a)
        hash_table_insert(ht, weights[index], index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
