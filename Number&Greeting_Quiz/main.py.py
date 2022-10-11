import random as rd

number_1 = [['일','이치'],
          ['이', '니'],
          ['삼', '산'],
          ['사', '욘'],
          ['오', '고'],
          ['육','로쿠'] ,
          ['칠', '나나'],
          ['팔', '하치'],
          ['구', '큐'],
          ['십', '쥬우'],
          ['십일', '쥬우이치'],
          ['십이', '쥬우니'],
          ]
number_2 = [['하나', '히토츠'],
            ['둘', '후타츠'],
            ['셋', '및츠'],
            ['넷', '욫츠'],
            ['다섯', '이츠츠'],
            ['여섯', '믗츠'],
            ['일곱', '나나츠'],
            ['여덟', '얓츠'],
            ['아홉', '코코노츠'],
            ['열', '토오']]

Others = [ ['아침인사', '오하요우'],
          ['점심인사', '곤니치와'],
          ['저녁인사', '곰방와'],
          ['감사해요', '아리가토우'],
          ['미안해요', '스미마센'],
          ['잘자', '오야스미'],
          ['잘가(안녕)', '사요우나라'],
          ['내일봐', '마타아시타']]

          

def NumberQuizOne():
    print("다음 나오는 숫자의 일본어 발음을 쓰시오(종료는 exit)")
    while(True):
        rnd = rd.randint(0, 11)
        answer = input(f"한국어 {number_1[rnd][0]} 는 일본어로 무엇인가요? -->")
        if answer == 'exit':
            return
        if answer == number_1[rnd][1]:
            print("정답입니다!\n\n")
        else:
            print("틀렸습니다!")
            print(f"정답은 {number_1[rnd][1]} 입니다.\n\n")

def NumberQuizTwo():
    print("다음 나오는 숫자의 일본어 발음을 쓰시오(종료는 exit)")
    while(True):
        rnd = rd.randint(0, 9)
        answer = input(f"한국어 {number_2[rnd][0]} 는 일본어로 무엇인가요? -->")
        if answer == 'exit':
            return
        if answer == number_2[rnd][1]:
            print("정답입니다!\n\n")
        else:
            print("틀렸습니다!")
            print(f"정답은 {number_2[rnd][1]} 입니다.\n\n")

def Other():
    print("다음 나오는 일상 단어의 일본어 발음을 쓰시오(종료는 exit)")
    while(True):
        rnd = rd.randint(0, 7)
        answer = input(f"{Others[rnd][0]} 는 일본어로 무엇인가요? -->")
        if answer == 'exit':
            return
        if answer == Others[rnd][1]:
            print("정답입니다!\n\n")
        else:
            print("틀렸습니다!")
            print(f"정답은 {Others[rnd][1]} 입니다.\n\n")
def Run(n):
    if n == 1:
        if int(input("어떤 버전으로 하시겠습니까? (1 -> 버전 1 / 2 -> 버전 2) --> ")) == 1:
            NumberQuizOne()
        else:
            NumberQuizTwo()
    elif n == 2:
        Other()

while(True):
    oper = int(input("실행할 일본어 퀴즈를 쓰시오(1 -> 숫자 / 2 -> 일상 단어 / 3 -> 종료)"))
    if oper == 3:
        break
    Run(oper)