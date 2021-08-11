security_num = "990310-1234567"

print("성별 : " + security_num[7])
#[x:y] : x부터 y직전까지
print("년도 : " + security_num[0:2])
print("월 : " + security_num[2:4])
print("일 : " + security_num[4:6])
#[:x] : 처음부터 x직전까지
print("생년월일 : " + security_num[:6])
#[x:] : x부터 끝까지
print("뒤 7자리 : " + security_num[7:])
#맨 뒤에서 7번째 끝까지
print("뒤 7자리 (뒤에서부터) : " + security_num[-7:])