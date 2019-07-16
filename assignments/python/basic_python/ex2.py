def recur_factorial(n):
    while n>=0:
        if (n==0 or n==1):
            return 1
        else:
            return n*recur_factorial(n-1)


if __name__ == "__main__":
    print(recur_factorial(3))