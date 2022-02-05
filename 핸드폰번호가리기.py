def solution(phone_number):
    answer = ''
    an = []
    for j in range(len(phone_number)-4):
        an.append('*')
    
    for k in range(len(phone_number)-4, len(phone_number)):
        an.append(phone_number[k])
        
    answer = ''.join(an)
    return answer
