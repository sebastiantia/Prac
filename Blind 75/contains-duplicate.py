def containsDuplicateValues(nums):
    #issue with this solution, time limit exceeds
    #it is important to search via keys instead of values
    dictionary = {}

    for i in range(len(nums)):
        if nums[i] in dictionary.values():
        
            return True

        dictionary[i] = nums[i]
        print(dictionary)

    return False

def containsDuplicate(nums):
    d ={}
    for i in range(len(nums)):
        if nums[i] in d:
            return True
        
        d[nums[i]] = 1

    return False


if __name__ == '__main__':
    nums = [1,23,5,6]
    print(containsDuplicate(nums))
