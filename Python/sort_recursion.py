sorted_list = []
def sorting(*args):
    lsts =[]
    lsts = list(args)
    unsorted_list = []
    smallest = 0
    for i in range (len(lsts)):
        cur_val = lsts[i]
        if(i == 0):
            smallest = lsts[i]
        else:
            if(smallest < cur_val):
                unsorted_list.append(cur_val)
            else:
                unsorted_list.append(smallest)
                smallest = cur_val
    sorted_list.append(smallest)
    lsts.remove(smallest)
    if (len(lsts) !=0):
        sorting(*unsorted_list)
    return (sorted_list)
