## String Processing | 문자열 처리

#### 문자열 처리 함수 | [string library](https://github.com/pup-paw/Python-Basics/blob/master/String/string_library.py)
  > `.lower()` 모든 글자를 소문자로 변환  
  > <br>
  > `.upper()` 모든 글자를 대문자로 변환  
  > <br>
  > `.isupper()` 해당 글자가 대문자인지 확인  
  > <br>
  > `.replace("a", "b")` 'a'를 'b'로 대체  
  > <br>
  > `.index("n")` 'n'의 첫 인덱스 반환 ('n'이 없으면 오류 발생)
  > <br>
  > `.index("n", i)` 'n'의 i 이상의 첫 인덱스 반환
  > <br>
  > `.find("n")` 'n'의 첫 인덱스 반환 ('n'이 없으면 -1 반환)
  > <br>
  > `.count("n")` 문자열 내 'n'의 개수를 반환


#### 슬라이싱 | [slicing](https://github.com/pup-paw/Python-Basics/blob/master/String/slicing.py)
  > `security_num[n]` n번째 글자  
  > <br>
  > `security_num[n:m]` n부터 m직전까지  
  > <br>
  > `security_num[:m]` 처음부터 m직전까지  
  > <br>
  > `security_num[n:]` n부터 끝까지  
  > <br>
  > `security_num[-n:]` 끝에서 n번째부터 끝까지  

#### 문자열 포맷 | [string format](https://github.com/pup-paw/Python-Basics/blob/master/String/stringFormat.py)
  > 방법 1
  > ``` python
  > print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))
  > ```
  > 방법 2
  > ``` python
  > print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
  > ```
  > 방법 3
  > ``` python
  > print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 23, color="보라"))
  > ```
  > 방법 4
  > ``` python
  > age = 20
  > color = "보라"
  > print(f"나는 {age}살이며, {color}색을 좋아해요.")
  > ```

#### 탈출문자 | [backslash](https://github.com/pup-paw/Python-Basics/blob/master/String/backslash.py)
  > `\n` 줄바꿈  
  > <br>
  > `\"` 문장 내에서 "  
  > <br>
  > `\\` 문장 내에서 \  
  > <br>
  > `\b` 백스페이스 (한글자 삭제)  
  > <br>
  > `\t` 탭  
