strD = """이번에는 \n 줄바꿈
문자열을
다중라인으로
저장
"""

# print(strD)

#인덱싱, 슬라이싱
strA = "python"
# print(strA[0])
# print(strA[:4])

# 함수(), class.메서드() 

#입력한대로 순서대로 출력 -> list[], 순서 상관없이 키:값으로 구성된 것 -> dic {}

#리스트와 다양한 메서드
colors = ["red", "blue", "green"]
# print(len(colors))
# print(colors[2])
# colors.append("black") #append 순서에 상관없이 추가하기
# print(colors)
# colors.insert(1,"white") #insert 원하는 순서에 추가하기 
# print(colors)
# colors.extend(["go", "back", "yes"]) #리스트 형식으로 추가
# print(colors)
# colors+=["red2"]
# print(colors)
colors.remove("red")
#print(colors)

#set 집합
#a = {'a', 'b', 'c', 'd'}
#b = {'c', 'd', 'e', 'f'}
#print(type(a))
#print(a.union(b)) #합집합 a|b
#print(a.intersection(b)) #교집합 a&b 
#print(a.difference(b)) #차집합 a-b

#튜플 리스트와는 달리 ()로 묶어서 표현하며 읽기 전용
#함수에서 하나 이상의 값을 리턴하는 경우
#문자열 포매팅
#print("id:%s, name:%s" %("kim", "김유신"))
# 리스트,세트,튜플을 이용해 서로 간에 언제든지 변환할 수 있다. list(),set(),tuple()

# tp = (1,2,3)
# print(len(tp))
# print(type(tp))
# print(tp[0])
# print(list(tp))
# print(set(tp))

#함수 정의 
#indentaion(들여쓰기)를 해야 하는 경우 코드의 끝 부분에 :를 표기한다. -> tap
# def calc(a,b):
#     return a+b,a*b
# a = calc(1,3)
# print(a)

# 형식 변환
#a = (10,20,30)
#b = list(a)
#b.append(40)
#print(b)
#c = tuple(b)
#print(c)

# 딕셔너리(dictionary)
# 자료의 수넛를 정할 수 없는 맵핑형, 키를 통한 빠른 검색 가능
# {key1 : value2, key2 : value2, ...}
# key 값을 가지고 입력, 수정, 삭제, 검색이 가능 -> 매우 실용적인 구조

# 메서드 ~.keys(), ~.values(), ~.items()

color = {'apple':'red', 'banana':'yellow', 'cherry':'red'}
# for item in color.items():
#     print(item)

# for k,v in color.items():
#   print(k,v)

# print( color["apple"])
#입력
color["melon"] = 'blue'
#수정
color["banana"] = 'red'
#삭제
del color["cherry"]
#print(color)

#print(color.keys()) #키만 출력 
#print(color.values()) #값만 출력

#c = color # color 와 c의 값이 같아지는게 아니라 같은 참조값을 가리키고 있다.

#모듈 - 메모리에서 여러 개의 함수가 정의되어 있는 1개의 파일
#패키지 - 여러 개의 모듈의 묶음(라이브러리)

#a = 2**10 # 제곱
#print(a)

#b = 1034//4 #몫
#print(b)

#tap 4칸

#for i in [1,2,3,4,5,6,7,8,9,10]:
#   print("*" * i)

# for k in range(10,20,3): #range 수열
#     print(k)
    
# print("---break---")
# first = [1,2,3,4,5,6,7,8,9,10]
# for i in first:
#     if i > 5:
#         break
#     print(i)

# print("---continue---")
# first = [1,2,3,4,5,6,7,8,9]
# for i in first:
#     if i > 4:
#         continue
#         print(i)
# print("---수열---")
# print(list(range(10)))
# print(list(range(1,12,2)))

print("---리스트 컴프리헨션---")
first = list(range(1,11))
print([i**2 for i in first if i>5])
tp = ("apple", "kiwi", "banana")
print([len(i) for i in tp if i == "kiwi"])

print("---필터링하는 경우---")
def getBiggerThan20(i): #함수 정의
    return i > 20

first = [10,20,30]
iterL = filter(getBiggerThan20, first)
for item in iterL:
    print(item)
