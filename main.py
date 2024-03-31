from basic_func import *


def main():
    a = array('i')
    filling_array(a, 3)
    print_array(a)
    print("Array is sorted in ascending order: ", is_sorted_ascending_order(a))
    print("Array is sorted in descending order: ", is_sorted_descending_order(a))


if __name__ == '__main__':
    main()
