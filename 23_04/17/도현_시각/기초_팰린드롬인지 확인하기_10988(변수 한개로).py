# https://solved.ac/profile/playdev7
# 문제 - 단어가 팰린드롬이면 1, 아니면 0을 출력하는 프로그램 만들기.
# 팰린드롬이란 앞으로 읽어도 뒤로 읽어도 똑같은 단어를 말한다.
# 기러기 토마토 스위스 인도인 별똥별 우0우! 를 팰린드롬이라고 한다.

# 도전 - 하나의 변수로 팰린드롬인지 확인하기.

# 우선 단어를 입력받는다.
word = input()

# 생각해보면 팰린드롬은 무조건 홀수여야만 한다.
# 그러면 길이에서 2로 나눈 몫 만큼 반복해서 인덱싱 해보면 어떨까?
# 왼쪽에서 오른쪽으로, 오른쪽에서 왼쪽으로.
for i in range(len(word)//2):

    # 팰린드롬이라면 [0] 과 [-1], [1]과 [-2], [2]와 [-3]이 같아야만 한다.
    # 왜냐하면 왼쪽의 첫 글자는 [0] 이고 오른쪽의 시작 글자는 [-1] 로 인덱싱이 되니까.
    
    # range() 문에서 i 변수는 0 1 2 등의 정수가 대입되므로 이를 이용해서 연산을 할 수도 있다.
    # 그러면 조건문을 이렇게 해보면 어떨까? [0-1] [-1-1] 처럼 오른쪽에서 왼쪽으로 읽어지지 않을까?!
    if word[i] == word[-i-1]:
        # 돌려보니 된다는 것을 알 수 있다. 그래서 조건을 만족하면 pass를 시키려고 한다.
        pass
        # TMI - 프로그래밍에서 i와 같은 변수를 "카운터 변수" 라고 한다.

    # pass를 시킨 이유는, if문의 조건에 해당하지 않을 때, else 일 때 무언갈 하기위해서다.
    # word[2]와 word[-3] 이 다른 단어인 그 순간! 처럼 팰린드롬이 아닐 때! 서로 다른단어일떄! 무언갈 하기 위해서다.
    else:
        print(0)
    # exit() 메소드를 통해서 프로그램을 바로 종료시킬 수 있다. break 문 보다 무서운 아이이다.
        exit()
    # 정리하면, 팰린드롬이 아닌 그 순간, else에 걸린 순간 바로 0을 출력하고 프로그램을 종료시키겠다는 뜻이다.

# 자, 그러면 여기까지 무사히 반복문을 통과해서 나왔다면?
# 여기까지 왔다면 if만을 통과한 팰린드롬이다.
# 그러니 1을 출력해주자.
print(1)