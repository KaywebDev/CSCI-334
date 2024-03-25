def quick_sort(list_to_sort, start=0, stop=None):

    comparisons = 0

    # initialize stop to the last valid index
    if stop is None:
        stop = len(list_to_sort) - 1

    logging.debug(f"List state: {list_to_sort}")
    logging.debug(f"Sorting from {start} to {stop} inclusive")

    # base case
    if stop-start <= 0:
        logging.debug("Base case")
        return comparisons
    # recursive case
    else:
        logging.debug("Recursive case")
        pivot_index = stop
        pivot = list_to_sort[pivot_index]
        logging.debug(f"Pivot value: {pivot}")

        left_index = start # "black arrow"
        right_index = pivot_index - 1 # "red arrow"

        # until the arrows cross
        while left_index <= right_index:

            comparisons += 1
            if list_to_sort[left_index] <= pivot:
                logging.debug(f"value at {left_index} is {list_to_sort[left_index]}, stays")
                left_index += 1
            else:
                logging.debug(f"value at {left_index} is {list_to_sort[left_index]}, greater than pivot, swapped with position {right_index}")
                swap(list_to_sort,left_index,right_index)
                right_index -= 1

        swap(list_to_sort,left_index,pivot_index)        

        logging.debug("Making recursive calls")
        l_comps = quick_sort(list_to_sort,start,left_index-1)
        r_comps = quick_sort(list_to_sort,left_index+1,stop)
        comparisons += l_comps
        comparisons += r_comps

        return comparisons