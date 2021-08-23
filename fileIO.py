#파일 쓰기1
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()
#파일 쓰기2
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()
#파일 전체 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()
#파일 한줄 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) #한줄 읽고 커서는 다음 줄로 이동(줄바꿈)
# print(score_file.readline(), end="") #줄바꿈 이용하지 않을 때
# print(score_file.readline())
# score_file.close()
#몇줄인지 모르는 파일 한줄씩 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readline() #list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()