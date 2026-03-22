"""
pandas DataFrame 数据结构详解与用法示例

DataFrame 是 pandas 的核心二维表格结构：
- 行：index（索引），默认 0,1,2...
- 列：columns（列名），每列是一种数据类型
- 可看作「带标签的二维数组」或「多个 Series 的字典」
"""
import pandas as pd
import numpy as np

def main():
    data = {
        "state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
    }
    frame = pd.DataFrame(data)
    print(frame)

    #只选取5行
    print(frame.head())

    # 只选取最后5行
    print(frame.tail())
    
    # 指定columns排列顺序
    print("**"*20)
    frame2 = pd.DataFrame(data, columns=["year", "state", "pop"])
    print(frame2)

    # 字典缺失缺少列
    print("**"*20)
    frame3 = pd.DataFrame(data, columns=["year", "state", "pop", "debt"]) # data 中缺少 debt 列
    print(frame3)
    

    # print(frame2['year'])

   # frame3.loc[2]
    #print(frame3.loc[1])
    
    print("**"*20)
    data1 = frame3.loc[1]
    data2 = frame3.iloc[1]
    print(data1)
    print(data2)
    print(data1.year)

def main2():
    data = {
        "state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
    }
    frame = pd.DataFrame(data)
    frame['eastern'] = frame.state == 'Ohio'
    print(frame) 
    del frame['eastern']
    print(frame)

def main3():
    populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
                    "Nevada": {2001: 2.4, 2002: 2.9, 2003: 3.2 }
                 }
    frame = pd.DataFrame(populations)   
    print(frame.T)
    print(frame)
   #data = np.ndarray(np.random(5,5))
    print(np.random.rand(5,5))
    print(np.arange(-5,5).reshape(5,5))

if __name__ == "__main__":
    main3()  