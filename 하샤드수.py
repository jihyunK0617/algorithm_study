def solution(x):
    answer = True
    
    to_x = str(x)
    total = 0
    
    for i in range(len(to_x)):
        total += int(to_x[i])
    
    if x%total != 0:
        answer = False
    return answer
