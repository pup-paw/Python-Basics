## Data Structure | 자료구조

#### 리스트 | [list](https://github.com/pup-paw/Python-Basics/tree/master/DataStructure/list.py)
  > 다양한 자료형 함께 사용 가능
  > ``` python
  > list = ["최지연", 23, True]  
  > ```
  > `.index("a")` 'a'의 인덱스 반환  
  > <br>
  > `.append("a")` 'a'를 마지막에 추가  
  > <br>
  > `insert(i, "a")` 'a'를 인덱스 i-1의 뒤, i의 앞에 추가   
  > <br>
  > `.pop()` 뒤에서 1개씩 반환하고 삭제함  
  > <br>
  > `.count("a")` 'a'의 개수 반환  
  > <br>
  > `.sort()` 정렬  
  > <br>
  > `.reverse()` 순서 뒤집기  
  > <br>
  > `.clear()` 모두 지우기  
  > <br>
  > `.extend(list2)` 기존 리스트에 list2를 추가하여 확장   

#### 사전 | [dictionary](https://github.com/pup-paw/Python-Basics/tree/master/DataStructure/dictionary.py)
  > key와 value 쌍으로 이루어짐
  > ```python
  > dictionary = {12:"최요키", 23:"최지연"}
  > ```
  > `dictionary[i]` key i의 value 반환 (value가 없는 key 입력시 오류 발생)  
  > <br>
  > `dictionary.get(i)` key i의 value 반환 (value가 없는 key 입력시 None 반환)  
  > `dictionary.get(i, "사용가능")` value가 없는 key 입력시 반환 기본 값 설정 가능  
  > <br>
  > `dictionary["a"] = "b"` key 'a'의 value에 'b' 입력 (key 'a'의 기존 value가 있을 시 'b'로 업데이트)  
  > <br>
  > `del dictionary[i]` key i의 value 삭제  
  > <br>
  > `.keys()` key들만 반환  
  > <br>
  > `.values()` value들만 반환  
  > <br>
  > `.items()` key, value 쌍으로 반환  
  > <br>
  > `.clear()` 초기화

#### 튜플 | [tuple](https://github.com/pup-paw/Python-Basics/tree/master/DataStructure/tuple.py)
  
#### 세트 | [set](https://github.com/pup-paw/Python-Basics/tree/master/DataStructure/set.py)

#### 자료구조의 변경 | [change_dataStructure](https://github.com/pup-paw/Python-Basics/tree/master/DataStructure/change_dataStructure.py)





