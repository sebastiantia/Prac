#smooth brain way
def productExceptSelfSmoothBrain(nums):
    answer = []
    counter = 0
    while counter < len(nums):
        product = 1
        for i in range(len(nums)):
            if i == counter:
                continue
            product *= nums[i]
        
        answer.append(product)
        counter += 1
        
    return answer

#must write in O(n) time
#use prefix and postfix arrays to save values before and after
def productExceptSelf(nums):
    prefix = []
    postfix = []
    prefix_sum = 1
    postfix_sum = 1
    
    for i in range(len(nums)):
        prefix_sum *= nums[i]
        prefix.insert(len(nums), prefix_sum)
        
    # prefix.insert(0, 1)
    # prefix.insert(len(nums), 1) 

        
    for i in range(len(nums)-1, -1, -1):
        postfix_sum *= nums[i]
        postfix.insert(0, postfix_sum)
        
    # postfix.insert(len(nums),1)
    # postfix.insert(0, 1)

    print(postfix) 
    print(prefix)

    answer = []
    
    for i in range(len(nums)):
        if i == 0:
            answer.insert(len(nums),postfix[i+1])
        elif i == len(nums)-1:
            answer.insert(len(nums), prefix[i-1])
        else:
            answer.insert(len(nums),prefix[i-1] * postfix[i+1])
    
    return answer

if __name__ == "__main__":
    nums = [1,3,5,7,8,9]

    print(productExceptSelf(nums))
