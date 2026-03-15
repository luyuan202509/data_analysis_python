"""
pandas Series 数据结构详解与用法示例

Series 是一维带标签数组：
- 可看作「带索引的一维数组」或「有序的键值对」
- DataFrame 的每一列就是一个 Series
"""
import pandas as pd
import numpy as np


def create_series():
    """1. 创建 Series 的多种方式"""
    print("=" * 50, "\n1. 创建 Series")

    # 方式一：从列表（默认整数索引 0,1,2,...）
    s1 = pd.Series([5, 6, 8, 4, 3, 2])
    print("从列表创建（默认索引）:\n", s1)

    # 指定索引 index
    s2 = pd.Series([10, 20, 30], index=["a", "b", "c"])
    print("\n指定 index:\n", s2)

    # 方式二：从字典（键→索引，值→数据）
    sdata = {"Ohio": 3500, "Texas": 7100, "Oregon": 1600, "Utah": 5000}
    s3 = pd.Series(sdata)
    print("\n从字典创建:\n", s3)

    # 字典 + 指定 index：只保留 index 中有的键，没有的为 NaN
    states = ["California", "Ohio", "Oregon", "Texas"]
    s4 = pd.Series(sdata, index=states)
    print("\n字典 + 指定 index（缺失键为 NaN）:\n", s4)
    print("是否缺失 pd.isnull(s4):\n", pd.isnull(s4))

    # 方式三：标量 + index（所有值相同）
    s5 = pd.Series(100, index=["x", "y", "z"])
    print("\n标量广播:\n", s5)

    # 方式四：从 NumPy 数组
    s6 = pd.Series(np.arange(4), index=["a", "b", "c", "d"])
    print("\n从 NumPy 数组:\n", s6)

    return s1, s2, s3, s4


def attributes_and_info(s: pd.Series):
    """2. 基本属性与信息"""
    print("\n" + "=" * 50, "\n2. 基本属性（以 s = pd.Series([5,6,8,4,3,2]) 为例）")
    s = pd.Series([5, 6, 8, 4, 3, 2])
    print("索引 s.index:", s.index.tolist())
    print("值 s.values:", s.values)
    print("底层数组 s.array:", s.array)
    print("长度 len(s):", len(s))
    print("数据类型 s.dtype:", s.dtype)
    print("名字 s.name:", s.name)
    s.name = "score"
    s.index.name = "id"
    print("设置 name 后:\n", s)
    print("\n描述统计 s.describe():\n", s.describe())


def indexing(s: pd.Series):
    """3. 数据访问：下标、loc、iloc、布尔"""
    print("\n" + "=" * 50, "\n3. 数据访问")
    s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])

    # 按索引标签
    print("s['b']:", s["b"])
    print("s[['a','c']]:\n", s[["a", "c"]])

    # 按整数位置：iloc
    print("s.iloc[0]:", s.iloc[0])
    print("s.iloc[1:3]:\n", s.iloc[1:3])

    # 按标签：loc（切片包含右端）
    print("s.loc['b':'d']:\n", s.loc["b":"d"])

    # 布尔索引
    print("s[s > 25]:\n", s[s > 25])


def operations(s: pd.Series):
    """4. 运算与对齐"""
    print("\n" + "=" * 50, "\n4. 运算与索引对齐")
    a = pd.Series([1, 2, 3], index=["x", "y", "z"])
    b = pd.Series([10, 20], index=["x", "y"])

    print("a + b（按索引对齐，缺失为 NaN）:\n", a + b)
    print("a * 2（标量广播）:\n", a * 2)
    print("a + 100:\n", a + 100)


def missing_and_drop(s: pd.Series):
    """5. 缺失值处理"""
    print("\n" + "=" * 50, "\n5. 缺失值")
    s = pd.Series([1, np.nan, 3, np.nan, 5])
    print("含 NaN 的 Series:\n", s)
    print("s.isna():\n", s.isna())
    print("s.dropna():\n", s.dropna())
    print("s.fillna(0):\n", s.fillna(0))


def series_and_dataframe():
    """6. Series 与 DataFrame 的关系"""
    print("\n" + "=" * 50, "\n6. Series 与 DataFrame")
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    print("DataFrame:\n", df)
    col_a = df["A"]
    print("\ndf['A'] 得到 Series:\n", col_a)
    print("type:", type(col_a))
    # Series 转 DataFrame（单列）
    back = col_a.to_frame()
    print("\nSeries.to_frame():\n", back)


def main():
    create_series()
    attributes_and_info(None)
    indexing(None)
    operations(None)
    missing_and_drop(None)
    series_and_dataframe()
    print("\n" + "=" * 50, "\n完成。")


if __name__ == "__main__":
    main()
