def solution(nums):
    answer = 0
    tmp = 0
    isOdd = 1
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                tmp = nums[i] + nums[j] + nums[k]
                for h in range(2,tmp):
                    # print(nums[i] , nums[j] , nums[k], tmp, h)
                    if tmp%h == 0:
                        isOdd = 0
                        break
                if isOdd == 1:
                    answer += 1
                isOdd = 1
                # print("answer = %d"%answer)
    
    return answer
