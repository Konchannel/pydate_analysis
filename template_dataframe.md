# DataFrame の扱い方

## (前提)
`import pandas as pd`

## DataFrameの宣言
values, index, columnsの順に宣言  
`
df = pd.DataFrame([[1, 2, None], [4, None, 6], [7, 8, 9]], 
    index=['i_0', 'i_1', 'i_2'], 
    columns=['c_0', 'c_1', 'c_2'])
`  

{index: value}, columnsの順に宣言  
※indexは宣言した順ではなく、アルファベット順(A~Z,a~z)に並ぶので注意  
`df2 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charry'], 
                    'Age': [20, 18, 9], 
                    'Hobby': ['Baseball', 'Game', 'Reading']}, 
                    index=['one', 'two', 'three'])`

## csvデータの読み込み
`df = pd.read_csv("sample.csv")`

## データの取得・変更
### データの値を全て取得
`df.values`

### データの値を一部取得
index名, column名を指定して1つだけ取得  
`df.at['i_0', 'c_1']`

index名, column名を指定して取得  
`df.loc[['i_0', 'i_2'], ['c_0', 'c_2']]`  
※ index, columnsの順に書く  

index番号, column番号を指定して取得  
`df.iloc[[0, 2], [0, 2]]`  
※ indexが0,2行目のcolumnが0,2行目のデータを返す  

`df.iloc[[0, 2], :]`  
※ indexが0,2行目のデータを返す(columnは全部指定)  

列に対して条件を指定して抽出  
`df.query('c_2 > 0')`  
`df.query('3.0 < c_2 < 7')`  
`df.query('c_0 in [None, 1, 2]')`  

インデックス(行)のみ取得  
`df.index`

カラム(列)のみ取得  
`df.columns`

### データの値を変更
データの値を1つだけ変更  
`df.at['i_1', 'c_0'] = None`  
`df.iat[1, 0] = None`

データの値を複数変更  
`df.loc[:, 'c_1'] = [10, 10, 10]`  


### インデックス(行)・カラム(列)を変更
一括変更  
`df2.index = ['i', 'ro', 'ha']`  
`df2.columns = ['tosi', 'syumi', 'namae']`  

カラム名を指定して変更  
`df2 = df2.rename(index={'one': 'zero'})`  
`df2 = df2.rename(columns={'Name': 'Last Name', 'Hobby': 'Pastime'})`  

関数で一括変更  
`df2 = df2.rename(index=str.title)`  
`df2 = df2.rename(columns=str.lower)`  
※str.titleで、英語の先頭だけ大文字にしている  

ラムダ式で変更  
`df2 = df2.rename(index=lambda s: s*3)`  
`df2 = df2.rename(columns=lambda s: 'it\'s'+ s)`  

## 欠損値の扱い
### 落とす
条件  
 - データ全体に対して欠損している数が少ないこと
 - 数値などのカテゴリであること（平均が取れなくなるなどの支障が想定される場合）  

コード  
特定のカテゴリがNaNならその行を削除  
`df2 = df.dropna(submit=['カテゴリ'])`

NaNが含まれる行を全て削除(カテゴリを指定しない)  
`df2 = df.dropna(submit=['カテゴリ'])`

実行後  
 - ['カテゴリ']列がNaNの行を削除したDataFrameとして返す
 
### 補間（埋める）
注意点
 - 欠損値が多い場合、ヒストグラムで見ると埋めた値の数値が突出して多くなり、偏ったデータに見える
 
コード  
指定した値で埋める  
`df.fillna(2000)`  

平均値で埋める  
`df.fillna(df.mean())`  
指定した列の欠損値を、その列の平均値で埋める
`df['c_1'].fillna(df['c_1'].mean())`
  
中央値で埋める  
`df.fillna(df.median())`  

