def solution(left, right):
    answer = 0
    
    count = 0 
    count_list = {}
    
    for i in range(left, right+1):
        for k in range(1,i+1):
            if i % k == 0:
                print(k)
                count += 1
        
        count_list[i] = count
        # count_list.append(count)
        count = 0
    
    # print(count_list)
    for j,h in count_list.items():
        if h % 2 == 0:
            answer += j
        else:
            answer -= j
    return answer
