def is_triplet(p,q,r):
    if((p+q > r) and (q+r > p) and (r+p>q)):
        return True
    return False

def triplet_exists(input_list=[]):
    input_list.sort()
    for p in range(len(input_list)-2):
        r = p+2
        q = p+1
        if (is_triplet(input_list[p],input_list[q],input_list[r])):
            return 1
    return 0

if __name__ == "__main__":
    a = [10,2,5,1,8,20]
    b = [10,50,5,2]

    print(triplet_exists(a))
    print(triplet_exists(b))