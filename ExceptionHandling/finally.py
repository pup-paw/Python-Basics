class BigNumberError(Exception):
    # pass
    def __init__(self, msg):
        self.msg = msg


try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요 : "))
    num2 = int(input("첫번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        #raise ValueError
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally:  # 에러 발생 여부와 상관 없이 무조건 실행
    print("계산기를 이용해 주셔서 감사합니다.")
