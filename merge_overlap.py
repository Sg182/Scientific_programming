
def merged_overlap(arr):

    arr.sort()
    merged_arr = [arr[0]]

    for i in range(1, len(arr)):

        if merged_arr[-1][1] >= arr[i][0]:
            merged_arr[-1][1] = max(merged_arr[-1][1], arr[i][1])
        else:
            merged_arr.append(arr[i])

    return merged_arr


if __name__ == "__main__":

    arr = [[1,3], [2,6], [8,10], [9,12]]

    print(merged_overlap(arr))
