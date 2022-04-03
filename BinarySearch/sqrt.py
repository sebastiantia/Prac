

def Sqrt(x):

    low, high = 0, x

    while low <= high:
        mid = (low + high)//2

        if mid * mid == x:
            return mid

        if mid * mid < x:
            
            sqrt = mid
            print("SQRT: ", sqrt)

            low = mid + 1
        else:
            high = mid - 1

        print("LOW: ", low)
        print("HIGH: ", high)

    return sqrt


if __name__ == "__main__":

    x = 6

    print(Sqrt(x))
