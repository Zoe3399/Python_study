# https://solved.ac/profile/playdev7

# m x n 행렬인데.. 아무튼 초콜릿을 생각하던, 행렬을 생각하던 다음과 같다.

# 2*2 행렬일 경우 row 1 번 column 2번
# 2*3 행렬일 경우 row 1 번 column 4번

# 3*2 행렬일 경우 row 2 번 column 3번
# 3*3 행렬일 경우 row 2 번 column 6번
# 3*4 행렬일 경우 row 2 번 column 9번

# 4*3 행렬일 경우 row 3 번 column 8번

# 다음과 같은 규칙을 찾을 수 있다.
# m은 m-1
# n은 (n-1)*m

# 근데 여기는 행이 n이므로
# n은 n-1
# m은 (m-1)*n
# 따라서 (n-1) + (m-1)*n 공식을 적용한다.

n, m = input().split()
n, m = int(n), int(m)

print((n-1) + (m-1)*n)