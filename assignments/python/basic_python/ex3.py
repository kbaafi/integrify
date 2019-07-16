def get_distinct_count(input_list):
    # a and b return the same value
    a = len({abs(i):abs(i) for i in input_list})
    b = len(set([abs(i) for i in input_list]))

    return a,b



if __name__ == "__main__":
    a = [1,-1,2,-2,3,4,5,6]
    print(get_distinct_count(a))

