cabinet = {3:"유재석", 100:"김태호"}

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#cabinet[]로 없는 값 출력시 오류 발생, 종료
#print(cabinet[5])
#.get()로 없는 값 출력시 None 반환
print(cabinet.get(5))
#.get() 이용시 없는 값 출력시 기본 값 설정 가능
print(cabinet.get(5, "사용 가능"))
print("hi")

#return boolean
print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["C-20"] = "조세호" #새로운 손님 추가
cabinet["A-3"] = "김종국" #기존 키의 값 빠지고 업데이트
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 쌍ㅇ로 출력
print(cabinet.items())

#목욕탕 폐점
cabinet.clear()
print(cabinet)