print("Python", "Java", "JavaScript", sep=" vs ")

print("Python", "Java", sep=",", end="?")
print("무엇이 더 재미있을까요?")

import sys
print("Python", "Java", file=sys.stdout) #표준 출력
print("Python", "Java", file=sys.stderr) #표준 에러

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    #ljust(n) : n자리를 확보한 뒤 왼쪽 정렬
    #rjust(n) : n자리를 확보한 뒤 오른쪽 정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":")

#은행 대기 순번표
#001, 002, 003, ...
for num in range(1,21):
    #zfill(n) : n자리를 확보한 뒤 값이 없으면 0으로 채움
    print("대기번호 : " + str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) #string
print("입력하신 값은 " + answer + "입니다.")