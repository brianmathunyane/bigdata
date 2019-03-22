def bubble_sort(items):

    count = 0

    for idx in range(len(items)-1):
        if items[idx] > items[idx + 1]:
            items[idx],items[idx + 1] = items[idx + 1],items[idx]
            count += 1

    if count == 0:
        return items
    else:
        return bubble_sort(items)



    '''Return array of items, sorted in ascending order'''


def merge_sort(items):

    len_i = len(items)
    # Base case. A list of size 1 is sorted.
    # Cae returns, so if reached then function will terminate after line 8
    if len_i == 1:
        return items
    # Recursive case. Find midpoint of list
    mid_point = int(len_i / 2)
    # divide list into two halves
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])
    # call merge_sort function on each half of list
    return merge(i1, i2)

def merge(A, B):
    new_list = []
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)

    if len(A) == 0:
        new_list = new_list + B
    if len(B) == 0:
        new_list = new_list + A

    return new_list


    '''Return array of items, sorted in ascending order'''


def quick_sort(items):
    if len(items) == 0:
        return items
    p = len(items) // 2
    l = [i for i in items if i < items[p]]
    m = [i for i in items if i == items[p]]
    r = [i for i in items if i > items[p]]
    return quick_sort(l) + m + quick_sort(r)
    '''Return array of items, sorted in ascending order'''
