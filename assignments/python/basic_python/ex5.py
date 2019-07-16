def get_missing(input_list = []):
    n = len(input_list)+1
    expected_sum = n*(n+1)/2
    actual_sum = sum(input_list)
    missing_number =  expected_sum - actual_sum
    return int(missing_number)


if __name__ == "__main__":
    a = [1,2,3,4,6,7,8,9]
    print(get_missing(a))