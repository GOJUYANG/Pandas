# ##Hello, world! 출력
# print 함수로 Hello, world!를 출력합니다.
# !
# print('HELLO, Jupyter Note!')
# HELLO, Jupyter Note!
# import pandas as pd
#
# data = {
#     'year': [2016,2017,2018],
#     'GDP rate': [2.8, 3.1, 3.0],
#     'GDP' : ['1.637M', '1.73M', '1.83M' ]
# }
#
# df = pd.dataFrame(data, index=data['year'])
#
# print(df)
# import pandas as pd
# ​
# data = {
#     'year': [2016,2017,2018],
#     'GDP rate': [2.8, 3.1, 3.0],
#     'GDP' : ['1.637M', '1.73M', '1.83M' ]
# }
# ​
# df = pd.dataFrame(data, index=data['year'])
# ​
# print(df)
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# Cell In[2], line 9
#       1 import pandas as pd
#       3 data = {
#       4     'year': [2016,2017,2018],
#       5     'GDP rate': [2.8, 3.1, 3.0],
#       6     'GDP' : ['1.637M', '1.73M', '1.83M' ]
#       7 }
# ----> 9 df = pd.dataFrame(data, index=data['year'])
#      11 print(df)
#
# File ~\anaconda3\lib\site-packages\pandas\__init__.py:264, in __getattr__(name)
#     260     from pandas.core.arrays.sparse import SparseArray as _SparseArray
#     262     return _SparseArray
# --> 264 raise AttributeError(f"module 'pandas' has no attribute '{name}'")
#
# AttributeError: module 'pandas' has no attribute 'dataFrame'
#
# import pandas as pd
# ​
# data = {
#     'year': [2016,2017,2018],
#     'GDP rate': [2.8, 3.1, 3.0],
#     'GDP' : ['1.637M', '1.73M', '1.83M' ]
# }
# ​
# df = pd.DataFrame(data, index=data['year'])
# ​
# print(df)
#       year  GDP rate     GDP
# 2016  2016       2.8  1.637M
# 2017  2017       3.1   1.73M
# 2018  2018       3.0   1.83M
# print("row labels:", df.index)
# print("row labels:", df.index)
# row labels: Int64Index([2016, 2017, 2018], dtype='int64')
# df = pd.DataFrame(data, index=data['year'])
# 에서 DataFrame은 2차원 데이터 생성을 의미하고
# 이때 (x,y)의 x는 만들고자 하는 데이터와 y는 행을 뜻한다.
# 해당 코드는 행 인덱스를 data=['year']의 리스트의 값을 이용하는 것이다.
# ​
# df.index가 가지는 의미는 데이터프레임의 행인덱스를 반환하는 것이다.
# 이때 dtype='int64'라는 것은 기본적으로 pandas는 정수형 인덱스를 생성할 때
# 32비트 정수를 사용하나 더 큰 범위의 정수를 다루어야할 때는 int64 데이터 타입을 선택한다고 한다.
# print("column lables:", df.columns)
# print("column lables:", df.columns)
# column lables: Index(['year', 'GDP rate', 'GDP'], dtype='object')
# print("head:", df.head())
# print("head:", df.head())
# head:       year  GDP rate     GDP
# 2016  2016       2.8  1.637M
# 2017  2017       3.1   1.73M
# 2018  2018       3.0   1.83M
# dtype='object' , 'object' 일반적으로 문자열 데이터를 의미한다. data.head()는 DataFrame의 처음 5개 행을 출력한다.
#
# print(df.year)
# 2016    2016
# 2017    2017
# 2018    2018
# Name: year, dtype: int64
# print(df[['year', 'GDP']])
# print(df[['year', 'GDP']])
#       year     GDP
# 2016  2016  1.637M
# 2017  2017   1.73M
# 2018  2018   1.83M
# df['year']는 'year'에 해당하는 Series를 반환한다. (1차원 데이터 구조) 반면에, df[['year', 'GDP']]는 'year', 'GDP'열에 해당하는 DataFrame을 반환한다.(2차원 데이터 구조)
#
# 두 개 이상의 열을 선택핮과 할때는 이중 대괄호를 사용해야한다. (규칙)
#
# print(df.loc[:1, ['year']])
# print(df.loc[:1, ['year']])
# Empty DataFrame
# Columns: [year]
# Index: []
# df.loc은 DataFrame에서 특정 행과 열을 선택하는 데 사용되는 인덱싱 방법이다. df.loc[x,['y']]에서 x는 행을 선택하고 'y'열을 선택하도록 지정한다는 뜻
#
# df.loc[:1, ['year']]는 첫번째 행부터 두번째 행까지의 데이터 중에서 'year'만 선택하라는 의미다.
#
# print("DataFrame shape:", df.shape)
# DataFrame shape: (3, 3)
# index_range = range(0,2)
# if all(i in df.index for i in index_range):
#     print("원하는 인덱스 범위에 해당하는 행이 존재한다.")
# else:
#     print("원하는 인덱스 범위에 해당하는 행이 존재하지 않는다.")
# 원하는 인덱스 범위에 해당하는 행이 존재하지 않는다.
# all(i in df.index for i in index_range) 는 파이썬의 내장함수 all()의 제너레이터 표현식이다.
#
# for i in index_range -> 인덱스 범위 내에 i가 순회하면서 i in df.index -> i가 df.index에 있는지 확인한다. 그리고 all()함수를 통해 모든 값(i)이 인덱스에 포함되어있다면 True를 반환한다.
#
# print(df[df['year'] == '2016'])
# Empty DataFrame
# Columns: [year, GDP rate, GDP]
# Index: []
# print(df.year.sum())
# 6051
# print(df.describe())
#          year  GDP rate
# count     3.0  3.000000
# mean   2017.0  2.966667
# std       1.0  0.152753
# min    2016.0  2.800000
# 25%    2016.5  2.900000
# 50%    2017.0  3.000000
# 75%    2017.5  3.050000
# max    2018.0  3.100000
# decribe()를 통해 기본적으로 제공되는 통계치가 모두 볼 수 있다