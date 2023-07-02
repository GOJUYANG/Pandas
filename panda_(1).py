# Pandas로 할 수 있는 일
# 1.Python 자료구조와의 호환(List ,Tuple, Dict, NumpyArray 등)
#      큰 데이터의 빠른 Indexing, Slicing, Sorting 하는 기능
import numpy as np
# 2.두 데이터 간의 Join(행,열 방향) 기능

# 3.데이터의 피봇팅 및 그룹핑

# 4.데이터의 통계 및 시각화 기능

# 5.외부 데이터를 입력 받아 Pandas 자료구조로 저장 및 출력(CSV, 구분자가 있는 txt, 엑셀데이터, SQL database, XML 등)

import pandas as pd

#1 list를 시리즈 형태로 변환
# li_data = ['2023-07-02', 3.14, 'ABC', 100, True]
# li_sr = pd.Series(li_data)
# print(li_sr)

#2 튜플을 시리즈 형태로 변환
# tu_data = ('python', '2023-07-02', '여', False)
# tu_sr = pd.Series(tu_data, index=['언어', '일자', '성별', '통과여부'])
# print(tu_sr)

#3 리스트를 DataFrame으로 생성
# data = [['go', 27], ['park', 25], ['kim',22]]
# df = pd.DataFrame(data, columns=['Name', 'Age'])
# print(df)

#4 dict을 DataFrame으로 생성
# data = {'Name': ['go', 'park', 'kim'], 'Age': [27,25,22]}
# df = pd.DataFrame(data) #따로 index, column을 지정하지 않고도 데이터프레임은 key값을 열로, value값을 데이터로 생성한다.
# print(df)

#5
# data = [{'a':1, 'b':2}, {'a':5, 'b':10, 'c':20}]
# df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
# print(df1) #c에 대한 column이 설정되어있지 않으므로 생성되지 않는다.

#6
# data = np.array([[1,2,3], [4,5,6]])
# df = pd.DataFrame(data, columns=['col1', 'col2', 'col3'])
# print(df)

#7 두 데이터 병합
df1 = pd.DataFrame({"idx_1": range(7),
                    'key': list("bbacaab")})
df2 = pd.DataFrame({"idx_2": range(3),
                    "key": list("abd")})
merge_on = pd.merge(df1, df2, on="key") #on 인자에는 공통적인 열명을 준다.
print(merge_on)
#병합 과정
# 'key'열을 기준으로 두 데이터를 매칭한다.
# 'key'열 값이 일치하는 행끼리 조합하여 새로운 행을 생성한다.
# 'key'가 'b'인 경우에 df1은 인덱스 0,1,6 / df2는 인덱스 1 행이 조합되어 생성되었다.
# df1의 c,d는 공통되는 값이 없기 때문에 생략한다.

merge_outer = pd.merge(df1, df2, how='outer') #key열의 값 중 한쪽 DF에만 있는 행들도 추가한다.
print(merge_outer) #동일한 행이 없는 경우 NaN로 표시한다.(Not a Number)


