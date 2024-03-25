def bubble_sort(list_to_sort):

    comparisons = 0

    last_unsorted_index = len(list_to_sort)-1
    swaps_occurred = True
    
    logging.debug(f"Bubble sort initial state: {list_to_sort}")

    # perform bubble passes until the first time we don't have to swap anything
    # worst-case scenario, this will be when we're down to just one item left
    while swaps_occurred:

        swaps_occurred = False
        
        logging.debug(f"Bubble sort pass on indexs up to {last_unsorted_index}")
        logging.debug(f"Pass initial state: {list_to_sort}")

        for i in range(last_unsorted_index):

            left_i = i
            right_i = i + 1

            # if the adjacent pair of values is out of order, swap them
            comparisons += 1
            if list_to_sort[left_i] > list_to_sort[right_i]:
                swap(list_to_sort,left_i,right_i)
                swaps_occurred = True
                logging.debug(f"{list_to_sort[left_i]}@{left_i} and {list_to_sort[right_i]}@{right_i} swapped")
                logging.debug(f"New list state: {list_to_sort}")
            else:
                logging.debug(f"{list_to_sort[left_i]}@{left_i} and {list_to_sort[right_i]}@{right_i} not swapped")

        # we've put the biggest remaining value at last_unsorted_index,
        # so we need to move it back by one
        last_unsorted_index -= 1
    
    logging.debug(f"No swaps performed last loop, final list state: {list_to_sort}")

    return comparisons