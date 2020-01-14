#!/usr/bin/python3

if __name__ == "__main__":
    import ast
    from merge import merge_overlapping_intervals
    
    array = input("Enter Interval array: ")
    print(merge_overlapping_intervals(list(ast.literal_eval(array))))