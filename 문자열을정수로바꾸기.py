def solution(s):
    answer = 0
    tmp = []
    if s[0] != '-' and s[0] != '+':
        answer = int(s)
    else:
        for j in range(1, len(s)):
            tmp.append(s[j])
        answer = int(''.join(tmp))
        if s[0] == '-':
            answer = answer * (-1)
    
    return answer
