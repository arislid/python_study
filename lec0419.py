'''
ttl =(10,20,30,40,50,60)
mylist=list(ttl)
mylist.append(70)
#ttl=tuple(mylist)

student1 = {'학번':1000, '이름':'홍길동', '학과':'파이썬', '학번':2000}

kpop = {'이름': '트와이스',
        '구성원수': 9,
        '대표곡':'signal',
        '맴버이름':'나연',
        '맴버이름1':'정연',
}

kpop['맴버이름2'] = '사나'

for k in kpop.keys():
    print('%s'%kpop[k])
    
foods = {'떡볶이':'오뎅',
         '짜장면':'단무지',
         '라면':'김치',
         '피자':'피클',
         '맥주':'땅콩',
         '치킨':'치킨무',
         '삼겹살':'상추'}


while True:
    myFood = input(str(list(foods.keys())) + " 중에서 좋아하는 음식은? ")
    if myFood in foods:
        print('%s -> %s '%(myFood, foods[myFood]))
    elif myFood == 'end':
        print('음식 궁합 종료')
        break
    else:
        print("그런 음식 없음")

myset1 = {1, 2, 3, 4, 5}
print(myset1)

saleslist =['삼각김밥', '바나나', '도시락', '삼각김밥', '삼각김밥', '도시락', '컵라면', '바나나']
saleslist2 = set(saleslist)
print(set(saleslist))
print()

numlist = [num for num in range(1, 6)]
numlist2 = []
for num in range(1,6):
    numlist2.append(num)

numlist3 = [num for num in range(1, 22) if (num%3 == 0)]

foods=['떡볶이', '짜장면', '라면', '피자', '치킨', '삽겹살']
sides=['오뎅', '단무지', '김치']
appetizers=['콜라', '맥주', '사이다', '막걸리']
for food, side, appetizer in zip(foods, sides, appetizers):
	print(food, '--->', side, '--->', appetizer)

dic = dict(zip(foods,sides))
tupList = list(zip(foods, sides))

oldlist=['짜장면', '탕수육', '군만두'] #reference 형식으로 저장
newlist = oldlist #얕은 복사, shallow copy
oldlist[0] = '짬뽕' # oldlist에 값을 넣었지만, newlist와 같은 주소이므로 newlist에 같은 값이 들어간다.

newlist1 = oldlist[:] #주소값이 서로 다르다. 깊은 복사!
oldlist[2] = '팔보채'

parking =[]
top =0
parking.append('자동차A')
top +=1
parking.append('자동차B')
top+=1
parking.append('자동차C')
top+=1
outcar = parking.pop()
top -=1
parking.append('자동차D')
top +=1
parking.append('자동차E')
print(parking)


ss='파이썬' + '최고'
print(ss)
ss='파이썬' * 3
print(ss)
print(ss[0])
print(ss[3:])
'''

## 변수 선언 부분 ##
inStr, outStr = "", ""
count, i = 0, 0

## 메인 코드 부분 ##
inStr = 'strong baby'
count = len(inStr)

for i in range(0, count) :
     outStr += inStr[count - (i + 1)]

print("내용을 거꾸로 출력 --> %s" % outStr)

sentence = 'Python is Easy. Therefore Programming is interesting!'
print(sentence.upper())
print(sentence.lower())

print(sentence.count('is'))
print(sentence.find('is'))
print(sentence.rfind('is'))
print(sentence.index('Therefore'))
print(sentence.endswith('!'))
print(sentence.strip())

