def merge_sort(list_to_sort):
    comp = 0
    if len(list_to_sort) > 1:
        mid_point = len(list_to_sort) // 2
        left_side = list_to_sort[:mid_point]
        right_side = list_to_sort[mid_point:]

        comp += merge_sort(left_side)
        comp += merge_sort(right_side)

        left_index, right_index, mid_index = 0, 0, 0

        while (left_index < len(left_side)) and (right_index < len(right_side)):
            if left_side[left_index] < right_side[right_index]:
                list_to_sort[mid_index] = left_side[left_index]
                left_index += 1
            else:
                list_to_sort[mid_index] = right_side[right_index]
                right_index += 1
            mid_index += 1

        while left_index < len(left_side):
            list_to_sort[mid_index] = left_side[left_index]
            left_index += 1
            mid_index += 1

        while right_index < len(right_side):
            list_to_sort[mid_index] = right_side[right_index]
            right_index += 1
            mid_index += 1

        comp += mid_index

    return comp