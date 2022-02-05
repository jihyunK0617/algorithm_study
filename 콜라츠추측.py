def solution(num):
    answer = 0
    
    count = 0
    answer = num

    while 1:

        if num == 1:
            return 0    
        elif answer%2 == 0:
            answer = answer / 2
        else:
            answer = answer * 3 + 1
            
        count += 1
        if answer == 1:
            answer = count
            break
        
        if count >= 500:
            answer = -1
            break

        
    
    return answer
