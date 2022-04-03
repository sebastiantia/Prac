

from tabnanny import check


def checkPerfectNumber(num):
    divisible = set()
    for i in range(1, num//2 +1):
        if num % i == 0 and i not in divisible:
            divisible.add(i)
            if i != 1:
                divisible.add(num//i)
    
    result = 0

    for i in divisible:
        result += i
    
    if result == num:
        return True
    
    return False

if __name__ == "__main__":
    print(checkPerfectNumber(28))
