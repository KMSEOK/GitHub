# n이 짝수인 경우 n을 2로 나눈다  if n % 2 == 0 짝수 2 / 2 == 0 4 / 2  = 2
# n이 홀수인 경우 n에 3곱하고 1 을 더한다 if n % 2 == 1 홀수  >>>> 3 * 3 + 1 = 10 1* 3+1  4 


def solution(num):
    answer = 0
    while num != 1:
        if num % 2 == 0 :
            num //= 2
        else :
            num = (num * 3) + 1
        answer += 1
        if answer >= 500 :
            answer = -1
            break
    return answer

print(solution(8))