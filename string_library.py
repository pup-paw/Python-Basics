python = "Python is Amazing"
#모든 글자를 소문자로 변환
print(python.lower())
#모든 글자를 대문자로 변환
print(python.upper())
#해당 글자가 대문자인지 확인
print(python[0].isupper())
#해당 문자열의 길이 반환
print(len(python))
#해당 글자를 명시된 글자로 대체
print(python.replace("Python", "Java"))

#해당 글자의 인덱스 반환
index = python.index("n")
print(index)
#미리 찾아둔 위치 다음의 인덱스부터 반환
index = python.index("n", index+1)
print(index)
#없으면 오류 발생
#print(python.index("Java"))

#해당 글자의 인덱스를 반환(없으면 -1 반환)
print(python.find("Java"))

#해당 글자의 개수를 반환
print(python.count("n"))
