def recur_increment(n):
    print(f"Value = {n}")
    if(n<5):
        recur_increment(n+1)
    if(n>=5 and n<8):
        recur_increment(n+(8-n))
    elif n>=8:
        print(f"Course passed with score {n}")

def check_is_valid(n):
    valid = False
    if n in range(11):
        print("Valid")
        valid = True
    return valid

def prompt_user_input():
    input_error_seen = True
    try:
        n = int(input("Please enter an integer between 0 and 10:  "))
        input_error_seen = False
    except Exception as e:
        input_error_seen = True
        n = -1
    return input_error_seen, n

if __name__ == "__main__":
    input_error_seen = True
    n = -1

    while input_error_seen==True or check_is_valid(n)==False :
        input_error_seen, n = prompt_user_input()

    recur_increment(int(n))