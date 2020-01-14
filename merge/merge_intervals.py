def merge_overlapping_intervals(invervals_list):
    assert all(isinstance(item,list) for item in invervals_list), (
        "Need a list like object. (eg). [[1,2], [3, 4]]"
    )
    sorted_list = sorted(invervals_list, key=lambda x: x[0])
    small, high = sorted_list.pop(0)
    merged = []
    for item in sorted_list:
        if item[0] > high:
            merged.append([small, high])
            small, high = item
        elif item[1] >= high:
            high = item[1]
    if [small, high] not in merged: merged.append([small, high])
    return merged