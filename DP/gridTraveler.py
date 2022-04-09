



def gridTraveler(r, c):
    if r == 0 or c == 0:
        return 0
    
    if r == 1 and c == 1:
        return 1

    return gridTraveler(r-1,c) + gridTraveler(r, c-1)


def memoization(r, c, Map):

    string = str(r) +", "+ str(c)
    alt = str(c) + ", " + str(r)

    # print(string)
    # print(Map) 
    if string in Map or alt in Map:
        return Map[string]
        
    if r == 0 or c == 0:
        return 0

    if r == 1 and c == 1:
        return 1

    Map[string] = memoization(r-1,c, Map) + memoization(r, c-1, Map)
    Map[alt] = Map[string] 

    return Map[string]



if __name__ == "__main__":

    Map = {}
    print(memoization(18,18, Map))

    r = 5
    c = 0

    string = str(c)

