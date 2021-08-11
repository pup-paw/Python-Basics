# 애완동물을 소개해 주세요
animal = "강아지"
name = "요키"
age = 12
hobby = "낮잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " +name + "입니다.")
hobby = "공놀이"
''' '+'로 문장을 이으면 str()로 형 변환 필요
 ','로 문장을 이으면 형 변환 필요x but, 한칸이 무조건 띄어짐'''
#print(name + "는 " + str(age) + "살이며, " + hobby + "를 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "를 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))