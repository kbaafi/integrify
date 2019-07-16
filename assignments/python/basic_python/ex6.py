def rotate(input_list,n):
    a = input_list
    for i in range(n):
        a= [a[-1]] + a[:-1]
    return a

if __name__ == "__main__":
    a = [1,2,3,4,5,6]
    print(rotate(a,3))