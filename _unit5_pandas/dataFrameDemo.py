"""
pandas DataFrame 数据结构详解与用法示例

DataFrame 是 pandas 的核心二维表格结构：
- 行：index（索引），默认 0,1,2...
- 列：columns（列名），每列是一种数据类型
- 可看作「带标签的二维数组」或「多个 Series 的字典」
"""
import pandas as pd
import numpy as np


def create_dataframe():
    """1. 创建 DataFrame 的多种方式"""
    print("=" * 50, "\n1. 创建 DataFrame")
    # 方式一：字典（键=列名，值=该列数据列表）
    data = {
        "state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2],
    }
    df = pd.DataFrame(data)
    print("从字典创建:\n", df)

    # 指定行索引
    df2 = pd.DataFrame(data, index=["a", "b", "c", "d", "e", "f"])
    print("\n指定 index:\n", df2)

    # 方式二：字典列表（每条字典是一行）
    rows = [
        {"name": "Alice", "age": 25, "city": "Beijing"},
        {"name": "Bob", "age": 30, "city": "Shanghai"},
    ]
    df3 = pd.DataFrame(rows,index=[1,2])
    print("\n从字典列表创建:\n", df3)
    return df

def attributes_and_info(df: pd.DataFrame):
    """2. 基本属性与信息"""
    print("\n" + "=" * 50, "\n2. 基本属性")
    print("列名:", df.columns.tolist())
    print("行索引:", df.index.tolist())
    print("形状 (行数, 列数):", df.shape)
    print("数据类型:\n", df.dtypes)
    print("\n前 3 行 head(3):\n", df.head(3))
    print("后 2 行 tail(2):\n", df.tail(2))
    print("\n描述性统计 describe():\n", df.describe())
    print("基本信息 info():\n")
    df.info()

def indexing(df: pd.DataFrame):
    """3. 数据访问：列、行、loc、iloc"""
    print("\n" + "=" * 50, "\n3. ===========数据访问======")

    # 取一列 → Series
    print("单列 df['state']:\n", df["state"])
    print("单列 df.year (属性式):\n", df.year)

    # 取多列 → 新 DataFrame
    print("\n多列 df[['state','pop']]:\n", df[["state", "pop"]])

    # 按行：loc 用标签，iloc 用整数位置
    print("\n第一行 loc[0]:", df.loc[0].tolist())
    print("前两行 iloc[:2]:\n", df.iloc[:2])
    print("第 2 行第 3 列 iloc[1,2]:", df.iloc[1, 2])

    # 布尔索引（筛选）
    print("\n筛选 year>=2002:\n", df[df["year"] >= 2002])
    print("筛选 state=='Ohio':\n", df[df["state"] == "Ohio"])


def modify_dataframe(df: pd.DataFrame):
    """4. 增删改列与排序"""
    print("\n" + "=" * 50, "\n4. 增删改与排序")

    # 新增列
    df = df.copy()
    df["pop_per_year"] = df["pop"] / (df["year"] - 1999)
    print("新增列 pop_per_year:\n", df)

    # 删除列（axis=1 表示列）
    df_drop = df.drop(columns=["pop_per_year"])
    print("\n删除列后:", df_drop.columns.tolist())

    # 排序：按列值
    print("\n按 year 升序:\n", df.sort_values("year"))
    print("按 pop 降序:\n", df.sort_values("pop", ascending=False))

    # 按多列排序
    print("\n先按 state 再按 year:\n", df.sort_values(["state", "year"]))


def main():
    #df = create_dataframe()
    #attributes_and_info(df)
    #indexing(df)
    #modify_dataframe(df)
    # print("\n" + "=" * 50, "\n完成。")
    pass 


def deleteSome():
    obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])
    print(obj)
    obj = obj.drop("c")
    print(obj)

def deleteSome2():
    data = pd.DataFrame(np.arange(16).reshape(4, 4),
                       index=["Ohio", "Colorado", "Utah", "New York"],
                       columns=["one", "two", "three", "four"])
    print(data)
    #data = data.drop(index=["Colorado", "Ohio"])
    data = data.drop("two",axis = 1)
    print(data)



if __name__ == "__main__":
    deleteSome2()  