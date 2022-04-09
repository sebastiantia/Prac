


def recursive(n):
    if n <= 2:
        return 1
    return recursive(n-1) + recursive(n-2)


#MEMOIZATION is the overarching strategy to solve Dynamic Programming Problems
#We will use a hash map, keys will be arg to fn, value will be return value

def dp(n, memo):

    if n in memo:
        return memo[n]

    if n == 0:
        return 0

    if n == 1:
        return 1

    memo[n] = dp(n-1, memo) + dp(n-2, memo)

    return memo[n]


if __name__ == "__main__":
    Map = {}
    print(dp(50, Map))