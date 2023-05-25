# https://solved.ac/profile/playdev7
# 10871 - X보다 작은 수

# 문제 - 정수 n개로 이루어진 수열 array에 대해 x보다 작은 수들을 공백으로 구분하여 출력하는 프로그램.
# 입력 - 정수의 개수 n 과 기준 숫자 x 가 입력된다.
# 다음 줄에 공백을 기준으로 array가 입력된다.
# 출력 - x보다 작은 수를 입력받은 순서대로 공백을 기준으로 구분하여 출력한다.

# 풀이 시작

n, x = map(int, input().split())
array = list(map(int, input().split()))

result = list()

# array를 순차적으로 대입하며 x보다 작은지 확인한다.
# 작다면, result에 추가한다.
for a in array:
    if a < x:
        result.append(a)

# 이후 result의 원소들을 순차적으로 출력한다.
# end 키워드를 통해 각 원소 사이에 공백이 출력되도록 한다.
for i in result:
    print(i, end=" ")